"""
Mini-Challenge: Let's begin HackGT by warming up your coding and hacking skills to get ready for the big coding challenges
ahead! Ever hear of Steganography? It may be a first for many, but Steganography is the practice of hiding a secret message
inside of something that is not secret, like a "digital image" insider another "digital image".

A "Digital Image" is a dot matrix data structure that represents a grid of pixels, so each pixel is the smallest individual
element of an image and provides variable color composed of three values (red, green and blue) which are 8 bit values or an
integer (32 bit) pixel. Check out the reference image here!

So each pixel can be represented with three values in binary code where the least significant bit is the rightmost bit and
has less impact on the final value and the leftmost bit is the most significant bit, so that, changes on the rightmost bits
will have a small visual impact on the digital image while any change on the leftmost bits will have a large impact on the
final value. Check out the reference image here!

Your mission (should you choose to accept it!) is to write the code that extracts and reveals the hidden secret image that
was hidden inside of the BlackRock logo by using its 2 most significant bits. You can download the image from
https://tinyurl.com/y5znb7kk.

SUBMIT TO: https://forms.gle/z2f7u9RosLjjLygJ7
"""

# Helpful links
# https://www.boiteaklou.fr/Steganography-Least-Significant-Bit.html
# https://stackoverflow.com/questions/1395356/how-can-i-make-bin30-return-00011110-instead-of-0b11110

from PIL import Image # package is named 'pillow' in Conda

# create a new copy to keep the reference file safe
im = Image.open("imageEmbedded.png")
im.save("imageDecrypted.png")
im = Image.open("imageDecrypted.png")

# get the pixels
width, height = im.size
pixels = im.load()

# loop thru the pixels and modify them
debug = True
for x in range(0,width):
    for y in range(0, height):
        if y % 100 == 0:
            debug = True
        else:
            debug = False

        r,g,b = pixels[x,y]
        if debug: print("[+] Pixel : [%d,%d]"%(x,y))
        if debug: print("[+] \tBefore : (%d,%d,%d)"%(r,g,b))

        # default values in case no bit has to be modified
        new_bit_red_pixel = 255
        new_bit_green_pixel = 255
        new_bit_blue_pixel = 255

        # red pixel
        r_bit = bin(r)[2:].zfill(8)  # bin() to get the binary value, [2:] to remove the leading '0b', zfill(8) to fill in any missing zeros
        n = int(len(r_bit) / 2)  # determine where to split ...will always be 4 thanks to zfill but still
        r_first_bit = r_bit[:n]  # get the first half of the byte
        r_last_bit = r_bit[n:]  # get the second half of the byte
        new_bit_red_pixel = int(str(r_last_bit)+str(r_first_bit), 2)  # rearrange the halves to find the secret
        if debug: print("[+] \tR: " + str(r_bit) + " " + str(r_first_bit) + " " + str(r_last_bit) + " " + bin(new_bit_red_pixel)[2:].zfill(8))

        # green pixel
        g_bit = bin(g)[2:].zfill(8)
        n = int(len(g_bit) / 2)
        g_first_bit = g_bit[:n]
        g_last_bit = g_bit[n:]
        new_bit_green_pixel = int(str(g_last_bit)+str(g_first_bit), 2)
        if debug: print("[+] \tG: " + str(g_bit) + " " + str(g_first_bit) + " " + str(g_last_bit) + " " + bin(new_bit_green_pixel)[2:].zfill(8))

        # blue pixel
        b_bit = bin(b)[2:].zfill(8)
        n = int(len(b_bit) / 2)
        b_first_bit = b_bit[:n]
        b_last_bit = b_bit[n:]
        new_bit_blue_pixel = int(str(b_last_bit)+str(b_first_bit), 2)
        if debug: print("[+] \tB: " + str(b_bit) + " " + str(b_first_bit) + " " + str(b_last_bit) + " " + bin(new_bit_blue_pixel)[2:].zfill(8))

        # place the modified pixel into the correct spot
        pixels[x,y] = (new_bit_red_pixel,new_bit_green_pixel,new_bit_blue_pixel)

        if debug: print("[+] \tAfter: (%d,%d,%d)"%(new_bit_red_pixel,new_bit_green_pixel,new_bit_blue_pixel))

im.save('imageDecrypted.png')