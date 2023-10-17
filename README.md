## Inspiration :
The inspiration for this project came from looking at the difficulty people with dyslexia face. I have a friend in my English class at the university whom I met recently and he actually has Dyslexia, I was curious about how a person with dyslexia reads or understands written language. After having a long conversation with him, I found out the accessibility features a person with dyslexia has access to, and whether it is effective. This gave me the inspiration to come up with a project to help people with dyslexia.

## What it does:
Ane-Lexia is a web application that assists students with Dyslexia. This is designed to convert handwritten images to readable text using a dyslexic-friendly font. This specialized font enhances readability for individuals with dyslexia. Additionally, the application incorporates a speech feature, allowing the converted text to be read aloud for hearing assistance. Through a combination of optical character recognition (OCR) technology with dyslexic-friendly typography and speech synthesis, the application provides valuable support to dyslexic students, ensuring accessibility and improving their learning experience. It scans the image provided, for example, notes on the board from a professor, and outputs it in a dyslexia-friendly text.

## How we built it:
We used Azure Vision API as our main OCR to convert image to text, we then used the text from the OCR as input and exported a pdf file with the text having OpenDyslexia font. We also created a text-to-speech converter to make it more accessible to people. We finally integrated the backend of Python using flask with HTML and CSS files, to create a web application.

## Challenges we ran into
One of the major challenges we ran into was finding an OCR that could detect handwriting. Our original plan was to use pytesseract, but it gave very bad results. We had to go through a ton of APIs to get one suitable to our needs. Another problem we ran into was formatting the text and downloading a .ttf file for OpenDyslexia, to export in the PDF. However, the biggest challenge was to integrate the backend and the front end.

## Accomplishments that we're proud of
We're amazingly proud of how minimalistic, straight to the point, and effective our app is. Based on some of our preliminary tests, we were getting almost 100% accuracy. What I'm most proud of is that we were able to create something that I am sure will be very helpful to a large population, and make their lives a little better.

## What we learned
The lessons I learned from this hackathon were very valuable. Since it was my first hackathon ever in my life I did not have any hope to even make this submission, all I wanted to do was have a great time and get better. But as me and my team started ideating and working on a project, our determination started becoming stronger and we were steadfast in making sure to submit something, and I am proud that we have come this far. So, the main lesson is, that if we have determination a seemingly impossible task can become possible to do.

## What's next for Ane-Lexia
Ane-Lexia will have a lot of things for it. We plan to have our own ML model to detect handwritten text, we also want to create iOS and Android apps to increase accessibility. We want to make our app easy to use and widely available to people who need it. I believe this will largely benefit the students in the education system who have dyslexia.

## Ane-Lexia License (Limited Use)

Ane-Lexia is an open-source project designed to assist students with dyslexia. This project is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND) License](https://creativecommons.org/licenses/by-nc-nd/4.0/).

### Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND) License

This work is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. To view a copy of this license, visit [https://creativecommons.org/licenses/by-nc-nd/4.0/](https://creativecommons.org/licenses/by-nc-nd/4.0/).

#### License Text

**You are free to:**

- Share — copy and redistribute the material in any medium or format for non-commercial purposes.
- The licensor cannot revoke these freedoms as long as you follow the license terms.

**Under the following terms:**

- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **NonCommercial** — You may not use the material for commercial purposes.
- **NoDerivatives** — If you remix, transform, or build upon the material, you may not distribute the modified material.

**No additional restrictions** — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

---

This license allows others to use your work as long as it's for non-commercial purposes, they provide appropriate attribution, and they do not create derivative works. It's important to note that this type of license can limit the potential for broader adoption and contribution to your project.

Please consult with a legal expert to ensure that the license you choose aligns with your intentions and is legally sound.
