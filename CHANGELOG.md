#0.2.0
_[ not for production ]_
- Fixes: Fix `dev` command not working inside the project directory
- Add SETTINGS: `DIPOR_PREFIX` (to help specify the base path of the project)
- Performance: Improve the perfrmance by only calling `get_structural_context` once
- BREAKING CHANGE: The scope of included templates have been changed. From now, templates only in the `_componenets` directory can be included. Instead of including like `{% include '_componenets/included_tpl.co' %}`, you can now write `{% include 'included_tpl.co' %}`
- A `_common` directory for templates reusable across all paths is now supported
- Note: Templates are first searched for in the current node's `_componenets` directory. If not found, searched in the `_common` directory.
- Internal Change: This should not affect the user of the package. Before, the routes was `{'name-of-route': '/path-to-route', None|{...}}`. Now it is `{'/path-to-route': 'name-of-route', None|{...}}`
- Feature Addition: Option to edit default route name to have customised and syntactically correct descritive text. This happend with the help of a `routes.yml` file.

#0.1.1
_[ not for production ]_
- Add support for custom port when serving files
- Add a cmd line utility `dipor bigbang [appname]` for minimal working playground
- Add a cmd line utility for hard build `dipor build [serve]`
- Add a cmd line utility for soft build `dipor dev [serve]`
- Update `dipor use <github-link>` for using themes
- Add a cmd line utility `dipor serve` to serve `public/` without running build
- Update `dipor_settings` path

#0.1.0
_[ not for production ]_
- The initial _not for production_ release
