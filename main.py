import requests, random, time, sys

total_amout = int(input("Enter total amount of promotions: "))

filesave = "".join(random.choices("au8wbynfd089ynm0a98hnzxicxb12439763517608123549031768478uwqiyuegsybutafxrnachsaeuicovsgvsgvpols", k=random.randint(5, 15)))

print(f"Running... Ctrl + C (x2) to stop the process (Saving to ./{filesave}.txt).")

with open(f"{filesave}.txt", "w") as save:
    added = 1
    retry = 0
    while added <= total_amout:
        try:
            save.write(requests.post(
                    url="https://api.discord.gx.games/v1/direct-fulfillment",
                    headers={
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"
                    },
                    json={
                        "partnerUserId": "".join(random.choices("qsqwxdnouzbqguiowsxcvgbewqcnwerpoisdbvmwrsfoih08t32y649r0650880239yrf09213891621513060170933458967492137ryhfduivghbneiwrdjhnocswdocuibasgh7980g49823v45g42m", k=64))
                    }
                ).json()["token"] + "\n")
            print(f"Token added. Progress: {added}/{total_amout}")
            added += 1
            retry = 0
        except:
            if retry > 10:
                print(f"RATE LIMITED. PLEASE TRY LATER. CANCELED AT {added}/{total_amout}.")
                sys.exit()
            print(f"Failed. Cooldown 2 seconds... Progress: {added}/{total_amout}")
            retry += 1
            time.sleep(2)
    
    print("Executed successfully.")