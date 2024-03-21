import requests

body = {
	"sitekey": "0x4AAAAAAAHWfmKCm7cUG869",
	"url": "https://rewards.bing.com/redeem/checkout?__RequestVerificationToken=CfDJ8I2_1MsyeC5LgSUu2RHmXGMv7UcTOTpMk7pWNX0nJhXzkpzDvELdQZ1KWM3nbNZmHqOnuGylIXM8cb4EBBJn31OnGBRvHY0Vo9UAXzL4GlhWEzK3Dr0GYyFiDHWv0w4O0nFSWQi485sDxLmTdFFhHnU4HCTKCsjSrQh-2LbCvrOfVLhyYspgL7jz0u6suKUlNA&variableAmount=12&productId=000800999996&variableSubmit=REDEEM+REWARD",
	"invisible": True
}

r = requests.post("https://turn.seized.live/solve", json=body)
token = r.json()["token"]
print("Solved :: " + token)