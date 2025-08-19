# MS Visiting Cards App

## Aim
We want to develop a simple one time API focussed app that can help us streamline collecting business data from visiting cards without much manual intervention

## Logic/Workflow

- We, as developers would receive a spreadsheet containing public Google drive URLs
- We need to crop the individual images from the collage files present in the google spreadsheet
- We need to feed the images to the API (limit 5), and then append the parsed the data to the spreadsheet (the same one shared with us) using sane column structure.

### API

#### Necessary Fields to handle/parse

- Name
- Role
- Org Name
- Org Address
- Org Phone Number
- Mobile
- Email
- Image/File Name
- File URL
