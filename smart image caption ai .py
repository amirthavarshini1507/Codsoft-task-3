import random
import datetime

class SmartImageCaptionAI:

    def __init__(self):

        self.history = []

        self.scenes = {
            "nature": {
                "captions": [
                    "A beautiful natural landscape with greenery.",
                    "Nature showing its beauty under open skies.",
                    "A peaceful outdoor environment."
                ],
                "mood": "Calm"
            },

            "city": {
                "captions": [
                    "A busy city filled with activity.",
                    "Urban life captured in a single frame.",
                    "Buildings and roads shaping the city."
                ],
                "mood": "Energetic"
            },

            "technology": {
                "captions": [
                    "A modern technology workspace.",
                    "Programming and innovation in action.",
                    "A smart digital environment."
                ],
                "mood": "Productive"
            },

            "education": {
                "captions": [
                    "Learning and growth in progress.",
                    "Students focused on gaining knowledge.",
                    "An educational environment."
                ],
                "mood": "Motivated"
            }
        }

    def analyze_image(self, category):

        category = category.lower()

        if category not in self.scenes:
            return None

        caption = random.choice(
            self.scenes[category]["captions"]
        )

        mood = self.scenes[category]["mood"]

        confidence = round(
            random.uniform(90, 99),
            2
        )

        result = {
            "category": category,
            "caption": caption,
            "mood": mood,
            "confidence": confidence,
            "time": str(datetime.datetime.now())
        }

        self.history.append(result)

        return result

    def statistics(self):

        print("\nIMAGE ANALYSIS STATISTICS")
        print("-" * 40)
        print("Total Images Analyzed:",
              len(self.history))

    def view_history(self):

        if len(self.history) == 0:
            print("\nNo records found.")
            return

        for i, item in enumerate(
                self.history, start=1):

            print(f"\nRecord {i}")
            print("Category:", item["category"])
            print("Caption:", item["caption"])
            print("Mood:", item["mood"])
            print("Confidence:",
                  item["confidence"], "%")

    def save_report(self):

        with open(
            "image_caption_report.txt",
            "w"
        ) as file:

            file.write(
                "SMART IMAGE CAPTION REPORT\n\n"
            )

            for item in self.history:

                file.write(
                    f"Category: {item['category']}\n"
                )

                file.write(
                    f"Caption: {item['caption']}\n"
                )

                file.write(
                    f"Mood: {item['mood']}\n"
                )

                file.write(
                    f"Confidence: {item['confidence']}%\n"
                )

                file.write(
                    "-" * 40 + "\n"
                )

        print(
            "\nReport Saved Successfully!"
        )


def main():

    ai = SmartImageCaptionAI()

    while True:

        print("\n" + "=" * 50)
        print("SMART AI IMAGE CAPTION GENERATOR")
        print("=" * 50)

        print("1. Analyze Image")
        print("2. View History")
        print("3. Statistics")
        print("4. Save Report")
        print("5. Exit")

        choice = input(
            "\nEnter Choice: "
        )

        if choice == "1":

            category = input(
                "\nEnter Category "
                "(nature/city/technology/education): "
            )

            result = ai.analyze_image(
                category
            )

            if result:

                print("\nIMAGE ANALYSIS RESULT")
                print("-" * 40)

                print(
                    "Category:",
                    result["category"]
                )

                print(
                    "Caption:",
                    result["caption"]
                )

                print(
                    "Mood:",
                    result["mood"]
                )

                print(
                    "Confidence:",
                    result["confidence"],
                    "%"
                )

            else:
                print(
                    "Invalid Category!"
                )

        elif choice == "2":
            ai.view_history()

        elif choice == "3":
            ai.statistics()

        elif choice == "4":
            ai.save_report()

        elif choice == "5":

            print(
                "\nThank You!"
            )
            break

        else:
            print(
                "Invalid Choice!"
            )


if __name__ == "__main__":
    main()