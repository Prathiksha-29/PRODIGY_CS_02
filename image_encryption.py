from PIL import Image

def xor_encrypt_decrypt(image, key):
    """Encrypt or decrypt an image using XOR operation with a given key."""
  
    img = Image.open(image)
    
    img = img.convert('RGB')
    pixels = img.load()
    
    width, height = img.size
    
    
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Apply XOR operation
            r = r ^ key
            g = g ^ key
            b = b ^ key
            pixels[x, y] = (r, g, b)
    
    return img

def save_image(img, output_path):
    """Save the processed image to the specified path."""
    img.save(output_path)
    print(f"Image saved to {output_path}")

def main():
    
    key = 123  # Key can be any integer between 0-255
    
   
    input_image_path = 'input_image.png'
    encrypted_image_path = 'encrypted_image.png'
    encrypted_img = xor_encrypt_decrypt(input_image_path, key)
    save_image(encrypted_img, encrypted_image_path)
    
   
    decrypted_image_path = 'decrypted_image.png'
    decrypted_img = xor_encrypt_decrypt(encrypted_image_path, key)
    save_image(decrypted_img, decrypted_image_path)

if __name__ == "__main__":
    main()
