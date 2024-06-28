# USBspeed

## Description:

USBspeed is a simple Python script designed to measure the write speed of a USB drive through 5 iterations. It was originally used to test the performance of USB extensions. While it primarily measures write speed, reading speed wasn't fully achievable due to caching issues on Windows. Despite this limitation, the script serves its intended purpose effectively.

## Limitations:

- Read Speed Measurement: Due to caching mechanisms on Windows, accurate read speed measurement wasn't possible as the system often reads from cache instead of the USB drive.
- Verification: The script's functionality for measuring write speed is straightforward and has been tested for its intended use case. However, for advanced or varied scenarios, additional testing may be required.

## Improvements:

- Cache Handling: Consider implementing cache flushing mechanisms if precise read speed measurement is critical.
- User Interface: Enhance user experience by adding clearer instructions and error handling.
- Documentation: Expand README to include troubleshooting tips and a more detailed explanation of the script's inner workings.

## Contributions:

Contributions and improvements to USBspeed are welcome. If you encounter issues or have ideas for enhancing its functionality, feel free to fork the repository and submit pull requests.

## Disclaimer:

I'm not a developer, so there may be room for improvement in the code quality and structure.
