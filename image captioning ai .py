import random
import datetime

class ImageCaptionAI:

    def __init__(self):

        self.history = []

        self.captions = {
            "dog": [
                "A dog is running in the park.",
                "A playful dog enjoying the outdoors.",
                "A dog running across green grass."
            ],

            "cat": [
                "A cat is sitting on a sofa.",
                "A cute cat looking at the camera.",
                "A cat relaxing indoors."
            ],

            "person": [
                "A person working on a laptop.",
                "Someone focusing on computer work.",
                "A person sitting at a desk."
            ],

            "car": [
                "A car parked beside the road.",
                "A vehicle moving on a street.",
                "A modern car in an urban area."
            ]
        }

    def generate_caption(self, object_name):

        if object_name.lower() in self.captions:

            caption = random.choice(
                self.captions[object_name.lower()]
            )

            confidence = round(
                random.uniform(85, 99),
                2
            )

            time_stamp = str(
                datetime.datetime.now()
            )

            result = {
                "object": object_name,
                "caption": caption,
                "confidence": confidence,
                "time": time_stamp
            }

            self.history.append(result)

            return result

        return None

    def display_history(self):

        print("\nCAPTION HISTORY")

        if len(self.history) == 0:
            print("No captions generated.")
            return

        for index, item in enumerate(
            self.history,
            start=1
        ):

            print(f"\nRecord {index}")
            print("Object :", item["object"])
            print("Caption :", item["caption"])
            print("Confidence :", item["confidence"], "%")
            print("Time :", item["time"])

    def save_report(self):

        file = open(
            "caption_report.txt",
            "w"
        )

        file.write(
            "IMAGE CAPTIONING REPORT\n\n"
        )

        for item in self.history:

            file.write(
                f"Object: {item['object']}\n"
            )

            file.write(
                f"Caption: {item['caption']}\n"
            )

            file.write(
                f"Confidence: {item['confidence']}%\n"
            )

            file.write(
                f"Time: {item['time']}\n"
            )

            file.write(
                "-" * 40 + "\n"
            )

        file.close()

        print(
            "\nReport saved successfully."
        )


def main():

    ai = ImageCaptionAI()

    while True:

        print("\n" + "=" * 50)
        print("AI IMAGE CAPTIONING SYSTEM")
        print("=" * 50)

        print("1. Generate Caption")
        print("2. View History")
        print("3. Save Report")
        print("4. Exit")

        choice = input(
            "\nEnter Choice: "
        )

        if choice == "1":

            image_object = input(
                "Enter detected object: "
            )

            result = ai.generate_caption(
                image_object
            )

            if result:

                print("\nGenerated Caption")
                print("-" * 30)

                print(
                    "Object:",
                    result["object"]
                )

                print(
                    "Caption:",
                    result["caption"]
                )

                print(
                    "Confidence:",
                    result["confidence"],
                    "%"
                )

            else:
                print(
                    "Object not found."
                )

        elif choice == "2":
            ai.display_history()

        elif choice == "3":
            ai.save_report()

        elif choice == "4":

            print(
                "\nThank You!"
            )

            break

        else:
            print(
                "Invalid Choice."
            )


if __name__ == "__main__":
    main()