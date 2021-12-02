

https://github.com/actions/upload-artifact/issues/51


https://stackoverflow.com/questions/46060010/download-github-release-with-curl


```
@oprypin try this:

$ curl -v -H "Authorization: token $SOME_TOKEN_WITHOUT_PERMISSIONS" https://api.github.com/repos/endless-sky/endless-sky/actions/artifacts/5036752/zip
you should get a Location header, among others. I don't have any special permissions to endless-sky/endless-sky, and this works for me.

OK so it works but the token must have public_repo access.



@oprypin huh? This works for me:

curl.exe `
--netrc-file C:\Users\Steven\_netrc `
-L `
-o crystal.zip `
https://api.github.com/repos/crystal-lang/crystal/actions/artifacts/60912181/zip
Where _netrc looks like this:

default login <USERNAME> password <PERSONAL ACCESS TOKEN>


# in order to download release artifacts from github, you have to first retreive the
# list of asset URLs using the github repo REST API. Use the asset URL to download 
# the artifact as a octet-stream data stream. You will need to get an access token 
# from "settings -> developer settings -> personal access tokens" on the github UI
#!/bin/bash -e

owner="MY_ORG_NAME"
repo="MY_REPO_NAME"
tag="ARTIFACT_TAG"
artifact="ARTIFACT_NAME"
token="MY_ACCESS_TOKEN"
list_asset_url="https://api.github.com/repos/${owner}/${repo}/releases/tags/${tag}?access_token=${token}"


# get url for artifact with name==$artifact
asset_url=$(curl "${list_asset_url}" | jq ".assets[] | select(.name==\"${artifact}\") | .url" | sed 's/\"//g')

# download the artifact
curl -vLJO -H 'Accept: application/octet-stream' \
     "${asset_url}?access_token=${token}"
```


