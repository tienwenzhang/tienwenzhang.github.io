# Final project

(1)

Download HTML template for your final project, and this template must satisfy the following conditions.

* more than three pages.

* each page must contains js, css, bootstrap/jquery, images.

* be satisfied with the purpose of FinTech

(2)

Create a project and app, and transfer your template to fit djnago structure.

# The attachment is an example for you to understand how to modify your template

## Project name: html_template

## Application name: main

~

### Git cloning into current directory
#### https://stackoverflow.com/questions/30556438/git-cloning-into-current-directory

git init
git remote add origin <remote_url>
git fetch --all --prune
git checkout master
git add -A .
git commit -m "Adding my files..."

In details:

You already have a remote repository and you want to add files to this repository.

    First you have to "tell" git that the current directory is a git repository
    git init

    Then you need to tell git what is the url of the remote repository
    git remote add origin <remote_url>

    Now you will need to grab the content of the remote repository (all the content - branches, tags etc) git fetch --all --prune

    Check out the desired branch (master in this example)
    git checkout <branch>

    Add the new files to the current <branch> git add -A .

    Commit your changes git commit

    Upload your changes back to the remote repository git push origin <branch>

