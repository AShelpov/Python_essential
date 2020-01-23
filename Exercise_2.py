seconds = int(input("Enter positive number of seconds: "))
residual_seconds = seconds
hour = residual_seconds // 3600
residual_seconds -= hour * 3600
minutes = residual_seconds // 60
residual_seconds = residual_seconds - minutes * 60

print(f"Amount of {seconds} seconds is equal to {hour} hours {minutes} minutes and {residual_seconds} seconds")
