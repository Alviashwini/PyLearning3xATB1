# real time example
browser = "edge"
match browser:
    case "chrome":
        print("execute the chrome browser")

    case "firefox":
        print("execute the firefox browser")
    case _:
        print("no idea")
browser = input("Enter the browser name\n")
match browser:
    case "chrome":
        print("chrome code executed")

    case "firefox":
        print("firefox code executed")
    case _:
        print("No browser found")
