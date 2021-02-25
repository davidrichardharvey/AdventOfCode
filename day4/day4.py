import re

fn = "day4input.txt"
required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid'] # Exclude 'cid'


def get_file_contents(filename):
    with open(filename) as file:
        contents = file.read()
    passports = contents.split('\n\n')
    passports = map(lambda x: x.replace('\n', ' ').split(' '), passports)
    return list(passports)


def passport_fields_present(passport: list) -> bool:
    approved = True
    passport_fields = [field[:3] for field in passport]
    for field in required_fields:
        if field not in passport_fields:
            approved = False
    return approved


def is_valid_passport(passport: list) -> bool:
    approved = True

    for field in passport:
        try:
            key, value = field.split(':')
            if key == 'byr':
                approved = 1920 <= int(value) <= 2002
            elif key == 'iyr':
                approved = 2010 <= int(value) <= 2020
            elif key == 'eyr':
                approved = 2020 <= int(value) <= 2030
            elif key == 'hgt':
                if value[-2:] == 'cm':
                    approved = 150 <= int(value[:3]) <= 193
                elif value[-2:] == 'in':
                    approved = 59 <= int(value[:2]) <= 76
                else:
                    approved = False
            elif key == 'hcl':
                approved = re.search(r"#([\w\d]){6}", value) is not None
            elif key == 'ecl':
                approved = value in ['amb','blu','brn','gry','grn','hzl','oth']
            elif key == 'pid':
                approved = len(value) == 9 and value.isdigit()
            elif key == 'cid':
                pass
            else:
                approved = False

            if not approved:
                return False
        except ValueError:
            return False

    return approved


pps = get_file_contents(fn)
print(pps)
counter = 0
for x in pps:
    if passport_fields_present(x):
        if is_valid_passport(x):
            counter += 1
print(counter)