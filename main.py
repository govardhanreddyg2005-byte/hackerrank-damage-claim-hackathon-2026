#imported csv module
import csv

def user_accountant(user_id):
    with open('dataset/claims.csv','r') as reader:
        csv_reader = csv.reader(reader)

        for row in csv_reader:
            user_id.append(row[0])

        return user_id
            
def image_path(path):

    with open('dataset/claims.csv','r') as reader:
        csv_reader = csv.reader(reader)

        for file in csv_reader:
            path.append(file[1].split(";"))

        return path

object_parts = {
    "car": {
        "car_parts": {
            "front_bumper", "rear_bumper", "door", "hood",
            "windshield", "side_mirror", "headlight",
            "taillight", "fender", "quarter_panel", "body"
        }
    },

    "laptop": {
        "laptop_parts": {
            "screen", "keyboard", "trackpad", "hinge",
            "lid", "corner", "port", "base", "body"
        }
    },

    "package": {
        "package_parts": {
            "box", "package_corner", "package_slide",
            "seal","label","contents", "item"
        }
    }
}

issue_types = {
    "dent",
    "scratch",
    "crack"
    "glass_shatter",
    "broken_part",
    "missing_part",
    "torn_packaging",
    "crushed_packaging",
    "water_damage",
    "stain"
}

detected = {
        "issue_type": "unknown",
        "object_part": "unknown"
    }

def detect_issue(users_claim):
    users_claim = users_claim.lower()
    
    for obj, data in object_parts.items():
        for parts_set in data.values():
            for part in parts_set:
                if part in users_claim:
                    detected["object_part"] = part
                    break

    for issue in issue_types:
        if issue in users_claim:
            detected["issue_type"] = issue
            break

    return detected


def main():

    claim = input("Customer: ")
    print(detect_issue(claim))

    user_ids = user_accountant([])

    image_paths = image_path([])

    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "user_id",
            "image_paths",
            "user_claim",
            "claim_object",
            "evidence_standard_met",
            "evidence_standard_met_reason",
            "risk_flags",
            "issue_type",
            "object_part",
            "claim_status",
            "claim_status_justification",
            "supporting_image_ids",
            "valid_image",
            "severity"

        ])

        writer.writerow([
            user_ids[0],
            *image_paths[0],
            claim,
            "false",
            "image analysis not implemented",
            "none",
            detected["issue_type"],
            detected["object_part"],
            "not_enough_information",
            "insufficient evidence",
            "none",
            "false",
            "unknown"

        ])

if __name__ == "__main__":
    main()
