# Setting up a remote action

## Overview

Github actions can be triggered remotely via the GitHub API.

## Instructions

### Setting up a Personal Access Token (PAT)

In order to allow an action to be triggered, you must create a fine-grained personal access token.

1. Click your profile picture then select Settings from the menu drawer.
2. Select `Developer Settings` from the bottom of the settings menu.
3. Under the `Personal access tokens` dropdown on the left, select `Fine-grained tokens`.
4. Click `Generate new token`
5. Configure the token:
    1. Assign a name and description.
    1. If you're making a token for an enterprise-owned repo, select the owner under `Resource owner`
    1. Set an expiration. Best practice is to keep this 90 days or less. No expiration is not recommended.
    1. Configure `Repository access`. It is recommended to apply this to one or as few repositories as necessary.
    1. Configure `Permissions`. Again, it is recommended to configure as few permissions as possible. To run an action, select the `Actions` Permission and set access to `Read and write`.
6. Click `Generate token`.

## Setting up a workflow

You will need to set up a workflow that runs on `workflow-dispatch`. For a barebones example, see .github/workflows/helloworld.yml.

## Triggering a workflow.

Once you have a workflow and a PAT, you can trigger the workflow using a curl request against the REST API:

```bash
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/OWNER/REPO/actions/workflows/WORKFLOW_ID/dispatches \
  -d '{"ref":"main"}'
```

You will need to past in your token for authorization, and replace OWNER, REPO and WORKFLOW_ID (this one will be the .yml for your action) with the values for your repo and action.

## Additional resources

[Workflow dispatch event](https://docs.github.com/en/rest/actions/workflows?apiVersion=2022-11-28#create-a-workflow-dispatch-event) \
[Managing personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens?apiVersion=2022-11-28&versionId=free-pro-team%40latest&productId=rest)
