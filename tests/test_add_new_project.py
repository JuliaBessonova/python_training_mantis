

def test_add_new_project(app):
    app.project.go_to_manage_page()
    app.project.open_projects_page()
    app.project.create()
    app.project.fill_project_form()
    app.project.submit_project_creation()
    app.project.return_to_projects_page()
