class ImageRecognizer:
    def __init__(self, image_data):
        self.image_data = image_data

    def recognize_pattern(self):
        height = len(self.image_data)
        width = len(self.image_data[0]) if height else 0

        if height == 3 and width == 4:
            return "Detected a basic pattern!"
        return "No recognizable pattern detected."

def get_user_input():
    print("Please enter the pixel values for a 3x4 image grid (0 or 255):")
    image_data = []
    for i in range(3):
        row = []
        for j in range(4):
            while True:
                try:
                    value = int(input(f"Pixel value at ({i+1},{j+1}): "))
                    if value in [0, 255]:
                        row.append(value)
                        break
                    else:
                        print("Invalid input. Please enter 0 or 255.")
                except ValueError:
                    print("Invalid input. Please enter an integer value.")
        image_data.append(row)
    return image_data

if __name__ == "__main__":
    user_image_data = get_user_input()

    recognizer = ImageRecognizer(user_image_data)
    result = recognizer.recognize_pattern()
    print(result)

