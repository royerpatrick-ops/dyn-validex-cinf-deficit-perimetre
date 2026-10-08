"""Validate archive integrity and exact recorded certificate; standard library only.

This checks the packaged record, not the mathematical proof. Reproduce the
calculation separately in a file outside this directory before comparing it.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import json


def validate(root):
    manifest = root / 'SHA256SUMS.txt'
    expected = {}
    for line in manifest.read_text(encoding='utf-8').splitlines():
        digest, name = line.split('  ', 1)
        path = root / name
        if Path(name).is_absolute() or '..' in Path(name).parts:
            raise ValueError('Unsafe manifest path: ' + name)
        if name in expected:
            raise ValueError('Duplicate manifest path: ' + name)
        expected[name] = digest
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError('Checksum mismatch: ' + name)
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*')
              if p.is_file() and p != manifest and '__pycache__' not in p.parts}
    if actual != set(expected):
        raise ValueError('File inventory differs from the manifest')
    data = json.loads((root/'results/CERTIFICATE.json').read_text())
    lo, hi = Fraction(data['C_lower']), Fraction(data['C_upper'])
    d_lo = Fraction(data['C_decimal_lower_outward'])
    d_hi = Fraction(data['C_decimal_upper_outward'])
    if not (d_lo < lo < hi < d_hi):
        raise ValueError('Decimal enclosure is not strictly outward')
    if not (Fraction('0.71923298') < lo < hi < Fraction('0.71923337')):
        raise ValueError('The manuscript enclosure is not implied')
    if not (Fraction('0.7192325') < lo < hi < Fraction('0.7192335')):
        raise ValueError('Six-decimal rounding is not certified')
    if data['J0'] != '141/140' or data['N'] != 100:
        raise ValueError('Unexpected certificate parameters')
    meta = json.loads((root/'metadata/zenodo_metadata_prepared.json').read_text())
    status = json.loads((root/'publication/PUBLICATION_STATUS.json').read_text())
    if meta['version'] != status['version'] or meta['license']['name'] != 'DEL 1.1 (custom)':
        raise ValueError('Inconsistent version or licence metadata')
    pdfs = list((root/'manuscript').glob('*.pdf'))
    if len(pdfs) != 1 or not pdfs[0].read_bytes().startswith(b'%PDF-'):
        raise ValueError('Principal manuscript PDF is missing or invalid')
    return {'checksummed_files':len(expected), 'exact_recorded_bounds_valid':True,
            'metadata_consistent':True, 'mathematical_proof_verified_by_this_program':False}


if __name__ == '__main__':
    result = validate(Path(__file__).resolve().parents[1])
    print(json.dumps(result, indent=2))
