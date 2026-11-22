from PIL import Image, ImageFilter, ImageEnhance

def image_utility():
    path = input("Enter image path: ")

    try:
        img = Image.open(path)
    except:
        print("Unable to open image!")
        return

    print("\n--- Digital Image Utility ---")
    print("1. Convert to Grayscale")
    print("2. Apply Blur Filter")
    print("3. Apply Sharpen Filter")
    print("4. Increase Brightness")
    print("5. Convert to RGB")
    print("6. Convert to HSV")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = img.convert("L")

    elif choice == "2":
        result = img.filter(ImageFilter.BLUR)

    elif choice == "3":
        result = img.filter(ImageFilter.SHARPEN)

    elif choice == "4":
        enhancer = ImageEnhance.Brightness(img)
        result = enhancer.enhance(1.5)

    elif choice == "5":
        result = img.convert("RGB")

    elif choice == "6":
        result = img.convert("HSV")

    else:
        print("Invalid choice!")
        return

    result.save("output_image.png")
    result.show()

    print("Image processed successfully!")
    print("Output saved as output_image.png")


image_utility()
