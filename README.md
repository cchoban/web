# Choban package manager


### Requirements
- Python & pip
- Node.js & npm
- yarn (optional)
- Postgres Database

### Database setup
Set these keys on your enviroment.
- DATABASE_HOST
- DATABASE_NAME
- DATABASE_USER
- DATABASE_PASSWORD
#### or
change `choban\settings.py` like this.

`DATABASE_HOST = os.environ.get('DATABASE_HOST') or 'YOUR HOST'`
`DATABASE_NAME = os.environ.get('DATABASE_NAME') or 'YOUR DATABASE NAME'`
`DATABASE_USER = os.environ.get('DATABASE_USER') or 'YOUR DATABASE USER'`
`DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD') or 'YOUR DB PASSWORD'`

### Install dependencies
1. Install pip dependencies with `pip install -r requirements.txt`
2. Install node dependencies
yarn:
`yarn`
npm:
`npm install`


### Installation
1. `python manage.py migrate`
2. `yarn dev` or `npm run dev`
3. `python manage.py runserver`
##### Custom configs
###### Disqus:
- from `app.js` edit `disqus_shortname` variable to your own disqus shortname.
