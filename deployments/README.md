
# Deployments

## Websites with Actions

Some advantages of using Actions:  

- ***Control over gemset***  
*Jekyll version* - Instead of using the currently enabled version at `3.9.0`, you can use any version of Jekyll you want. For example `4.3.2`,  
or point directly to the repository.  
*Plugins* - You can use any Jekyll plugins irrespective of them being on the supported versions list, even `*.rb` files placed in the `_plugins`  
directory of your site.  
*Themes* -While using a custom theme is possible without Actions, it is now simpler.

- ***Workflow Management***  
*Customization* - By creating a workflow file to run Actions, you can specify custom build steps, use environment variables.  
*Logging* - The build log is visible and can be tweaked to be verbose, so it is much easire to debug errors using Actions.

- ***WOrkspace setup***  
The first and foremost requirement is a Jekyll project hosted at GitHub. We are only going to cover builds from the `main` branch here. Therefore,  
ensure that you are working on the `main` branch, Whe the Action builds your site, the contents of the *destination* directory will be automatically  
pushed to the `gh-pages` branch with a commit, ready to be used for serving.

### Setting up the Action

GitHub Actions are registered for a repository by using a YAML file inside the directory path `.github/workflows`. For simplicity, here we use one of  
the *Jekyll Actions* to show you how to use the action.

Create a *workflow file*, `github-pages.yml`, using either the GitHub interface or by pushing a YAML file to the workflow directory path manually.  

