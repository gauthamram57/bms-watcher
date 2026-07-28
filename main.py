from src.watcher import check_booking
from src.notifier import send_telegram

URL = "https://in.bookmyshow.com/cinemas/COIM/pvr-brookefields-mall-coimbatore/buytickets/PBMC/20260801"

print("Checking BookMyShow...")

if check_booking(URL):
    print("Bookings OPEN!")

    send_telegram(
        "🎉 Saturday bookings are OPEN!\n\n"
        + URL
    )

else:
    print("Bookings not open.")
