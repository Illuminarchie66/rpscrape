from pathlib import Path
from orjson import loads

ROOT_DIR = Path(__file__).resolve().parents[2]

REGIONS_FILE = ROOT_DIR / 'courses' / '_regions'
_regions = loads(REGIONS_FILE.read_text())

ROOT_DIR = Path(__file__).resolve().parents[2]

COURSES_FILE = ROOT_DIR / 'courses' / '_courses'
_courses = loads(COURSES_FILE.read_text())

def get_region(course_id: str) -> str:

    courses = _courses.copy()
    courses.pop('all')

    for region, course in courses.items():
        for _id in course.keys():
            if _id == course_id:
                return region.upper()

    return ''


def print_region(code: str, region: str):
    print(f'\tCODE: {code: <4} |  {region}')


def print_regions():
    for code, region in _regions.items():
        print_region(code, region)


def region_search(term: str):
    for code, region in _regions.items():
        if term.lower() in region.lower():
            print_region(code, region)


def valid_region(code: str) -> bool:
    return code in _regions
