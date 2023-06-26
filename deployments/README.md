
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

### Providing permissions

At the start of each workflow run, GitHub automatically creates a unique `GITHUB_TOKEN` secret to use in your workflow. You can use the `GITHUB_TOKEN`  
to authenticate in a workflow run. You can use the `GITHUB_TOKEN` by using the standard syntax for referencing secrets: `$`, For more info:  
<https://docs.github.com/en/actions/security-guides/automatic-token-authentication>

If you need a token that requires permission that aren't available in the `GITHUB_TOKEN`, you can create a Personal Access Token (PAT), and set it as  
a secret in your repository for this action to push to the gh-pages branch:  

### Build and deploy

On pushing any local changes onto `main`, the action will be triggered and the build will *start*.

To watch the progress and see any build errors, check on the build *status* using one of the following approaches:  
- *View by commit*  
Go to the repository level view in GitHub. Under the most recent commit (neat thr top) you'll see a *status symbol* next to the  
commit message as a tick or X. Hover over it and click the *details* link
- *Actions tab*  
Go to the repository's Actions tab. Click on the `jekyll` workflow tab

If all goes well :), all steps will be green and built assets will now exist on the gh-pages branch

On a succesful build, GitHub Pages will *publish* the site stores on the repository `gh-pages` branches. Note that you do not need to setup a  
`gh-pages` branch or enable GitHub Pages, as the action will take care of this for you. (For private repositories, you will have to upgrade to a paid  
plan).


