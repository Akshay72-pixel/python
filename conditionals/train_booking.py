seat_type = input("Enter the seat type(sleeper/AC/general/luxury) = ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper seat cost 200")
    case "ac":
        print("AC seat cost 150")
    case "general":
        print("General seat cost 50")
    case "luxury":
        print("Luxury seat cost 500")
    case _:
        print(f"No seat avialabel for {seat_type}")