# Project wise assets.

src>assets directory
=====================
This directory contains the static assets one is public and one is src, which will used over the entire project.

`src` directory contains all the unminified source file(css, sass, es6, typescript and many more)
`public` directory contains all the minified output file(css and js)


Directory structure
=====================
docs: project documentation, hows to.
src: source code for frontend as well as backend.
src> assets: contains the static files
src>assets>src: contains the static files for development mode
src>assets>public: contains static files for production mode, inface `base.html` will consume the
static files from this `assets/public/` directory.

media: use for storing the media(on other server)
static:(use for storing the static files, infact when you run './manage.py collectstatic` command the conent of
`src/assets/public` are copied here.

node_modules: Node modules directory for front-end dependencies

pustakalaya_apps: directory that contains all the django apps.

templates: Overall project template.

Dockerfile: file to describe project image.

manage.py: django python utility to create apps.

package.json: frontend lib dependencies tree.

webpack.config.js: webpack configuration file.


