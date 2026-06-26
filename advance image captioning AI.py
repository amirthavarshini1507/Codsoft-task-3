import random
import datetime

class AdvancedImageCaptionAI:

    def __init__(self):

        self.history = []

        self.database = {
            "nature": {
                "captions": [
                    "A beautiful landscape surrounded by greenery.",
                    "A peaceful natural scene under the open sky.",
                    "Nature displaying its beauty and serenity."
                ],
                "emotion": "Calm"
            },

            "technology": {
                "captions": [
                    "A modern workspace focused on innovation.",
                    "Technology driving creativity and productivity.",
                    "A smart digital environment."
                ],
                "emotion": "Focused"
            },

            "city": {
                "captions": [
                    "A vibrant city full of activity.",
                    "Urban life captured in motion.",
                    "A modern city landscape."
                ],
                "emotion": "Energetic"
            }
        }

    def generate_caption(self, category):

        if category not in self.database:
            return None

        caption = random.choice(
            self.database[category]["captions"]
        )

        emotion = self.database[category]["emotion"]

        confidence = round(
            random.uniform(90, 99),
            2
        )

        keywords = caption.split()[:4]

        record = {
            "category": category,
            "caption": caption,
            "emotion": emotion,
            "confidence": confidence,
            "keywords": keywords,
            "time": str(datetime.datetime.now())
        }

        self.history.append(record)

        return record

    def view_history(self):

        if not self.history:
            print("\nNo records found.")
            return

        for i, item in enumerate(self.history, 1):

            print("\n" + "=" * 40)
            print("Record", i)
            print("=" * 40)

            print("Category :", item["category"])
            print("Caption  :", item["caption"])
            print("Emotion  :", item["emotion"])
            print("Keywords :", ", ".join(item["keywords"]))
            print("Confidence :", item["confidence"], "%")

    def search_caption(self, word):

        found = False

        for item in self.history:

            if word.lower() in item["caption"].lower():

                print("\nFound:")
                print(item["caption"])
                found = True

        if not found:
            print("\nNo matching captions found.")

    def statistics(self):

        print("\nIMAGE ANALYTICS")
        print("-" * 40)

        print("Total Images Processed:",
              len(self.history))

        if len(self.history) > 0:

            avg = sum(
                item["confidence"]
                for item in self.history
            ) / len(self.history)

            print(
                "Average Confidence:",
                round(avg, 2),
                "%"
            )

    def save_report(self):

        with open(
            "analytics_report.txt",
            "w"
        ) as file:

            file.write(
                "ADVANCED IMAGE CAPTION REPORT\n\n"
            )

            for item in self.history:

                file.write(
                    f"Category: {item['category']}\n"
                )

                file.write(
                    f"Caption: {item['caption']}\n"
                )

                file.write(
                    f"Emotion: {item['emotion']}\n"
                )

                file.write(
                    f"Confidence: {item['confidence']}%\n"
                )

                file.write(
                    "-" * 50 + "\n"
                )

        print(
            "\nReport Saved Successfully!"
        )


def main():

    ai = AdvancedImageCaptionAI()

    while True:

        print("\n" + "=" * 50)
        print("ADVANCED AI IMAGE CAPTIONING SYSTEM")
        print("=" * 50)

        print("1. Generate Caption")
        print("2. View History")
        print("3. Search Captions")
        print("4. Analytics")
        print("5. Save Report")
        print("6. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":

            category = input(
                "\nEnter Category "
                "(nature/technology/city): "
            )

            result = ai.generate_caption(
                category
            )

            if result:

                print("\nCAPTION GENERATED")
                print("-" * 40)

                print(
                    "Caption:",
                    result["caption"]
                )

                print(
                    "Emotion:",
                    result["emotion"]
                )

                print(
                    "Keywords:",
                    ", ".join(
                        result["keywords"]
                    )
                )

                print(
                    "Confidence:",
                    result["confidence"],
                    "%"
                )

            else:
                print("Invalid Category!")

        elif choice == "2":
            ai.view_history()

        elif choice == "3":

            word = input(
                "Enter keyword: "
            )

            ai.search_caption(word)

        elif choice == "4":
            ai.statistics()

        elif choice == "5":
            ai.save_report()

        elif choice == "6":

            print("\nThank You!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()