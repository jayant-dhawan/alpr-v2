# alpr-web

Project made for Hackathon at Codinova Technologies

DEMO -> [click here](https://alpr-v2.herokuapp.com/)

## Tech Used:

- Backend
    - Python
    - FastApi
    - OpenCV
    - Pytesseract
- Frontend
    - VueJS
    - Pico CSS
- Deployment
    - Heroku
- Testing
    - Pytest

## How image recognition is implemeted

- OpenCV is a library of programming functions mainly aimed at real-time computer vision. It's Haar Cascade classifier is used to idetify the license plate in the image. Model used for the classifier can be found at `/app/dependencies/indian_license_plate.xml` (Couldn't find the source for the model).
- OpenCV is used to refine the charaters in the extracted plate.
- Pytesseract, a wrapper for Tessaract which is an OCR library by Google. It is used to read the characters from the extracted plate.

## License

This project is licensed under the terms of the GNU license.
