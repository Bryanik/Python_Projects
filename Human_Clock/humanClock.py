#!/usr/bin/env python3

import sys

def format_duration(seconds):
    if isinstance(seconds, int) and not isinstance(seconds, float) and seconds >= 0:
        if seconds == 0:
            return "now"
        elif seconds < 60:
            #seconds
            sec = seconds
            if sec == 1:
                return "1 second"
            elif sec > 1:
                return f"{sec} seconds"
                print(f"{sec} seconds")
        elif seconds < 3600:
            #minutes
            min = seconds // 60
            sec = seconds % 60
            if min == 1 and sec == 0:
                return "1 minute"
            elif min == 1 and sec == 1:
                return f"1 minute and 1 second"
            elif min == 1 and sec > 1:
                return f"1 minute and {sec} seconds"
            elif min > 1 and sec == 0:
                return f"{min} minutes"
            elif min > 1 and sec == 1:
                return f"{min} minutes and 1 second"
            elif min > 1 and sec > 1:
                return f"{min} minutes and {sec} seconds"
        elif seconds < 86400:
            #hours
            hr = seconds // 3600
            rsec = seconds % 3600
            min = rsec // 60
            sec = rsec % 60
            if hr == 1 and min == 0 and sec == 0:
                return "1 hour"
            elif hr == 1 and min == 0 and sec == 1:
                return "1 hour and 1 second"
            elif hr == 1 and min == 1 and sec == 0:
                return "1 hour and 1 minute"
            elif hr == 1 and min == 1 and sec == 1:
                return "1 hour, 1 minute and 1 second"
            elif hr == 1 and min == 1 and sec > 1:
                return f"1 hour, 1 minute and {sec} seconds"
            elif hr == 1 and min > 1 and sec == 0:
                return f"1 hour and {min} minutes"
            elif hr == 1 and min > 1 and sec == 1:
                return f"1 hour, {min} minutes and 1 second"
            elif hr == 1 and min > 1 and sec > 1:
                return f"1 hour, {min} minutes and {sec} seconds"
            elif hr > 1 and min == 0 and sec == 0:
                return f"{hr} hours"
            elif hr > 1 and min == 0 and sec == 1:
                return f"{hr} hours and 1 second"
            elif hr > 1 and min == 1 and sec == 0:
                return f"{hr} hours and 1 minute"
            elif hr > 1 and min == 1 and sec == 1:
                return f"{hr} hours, 1 minute and 1 second"
            elif hr > 1 and min == 1 and sec > 1:
                return f"{hr} hours, 1 minute and {sec} seconds"
            elif hr > 1 and min > 1 and sec == 0:
                return f"{hr} hours and {min} minutes"
            elif hr > 1 and min > 1 and sec == 1:
                return f"{hr} hours, {min} minutes and 1 second"
            elif hr > 1 and min > 1 and sec > 1:
                return f"{hr} hours, {min} minutes and {sec} seconds"
            
        elif seconds < 31536000:
            #days
            day = seconds // 86400
            rsec = seconds % 86400
            hr = rsec // 3600
            rsec2 = rsec % 3600
            min = rsec2 // 60
            sec = rsec2 % 60
            if day == 1 and hr == 0 and min == 0 and sec == 0:
                return "1 day"
            elif day == 1 and hr == 0 and min == 0 and sec == 1:
                return "1 day and 1 second"
            elif day == 1 and hr == 0 and min == 1 and sec == 0:
                return "1 day and 1 minute"
            elif day == 1 and hr == 0 and min == 1 and sec == 1:
                return "1 day, 1 minute and 1 second"
            elif day == 1 and hr == 0 and min == 1 and sec > 1:
                return f"1 day, 1 minute and {sec} seconds"
            elif day == 1 and hr == 0 and min > 1 and sec == 0:
                return f"1 day and {min} minutes"
            elif day == 1 and hr == 0 and min > 1 and sec == 1:
                return f"1 day, {min} minutes and 1 second"
            elif day == 1 and hr == 0 and min > 1 and sec > 1:
                return f"1 day, {min} minutes and {sec} seconds"
            
            elif day == 1 and hr == 1 and min == 0 and sec == 0:
                return "1 day and 1 hour"
            elif day == 1 and hr == 1 and min == 0 and sec == 1:
                return "1 day, 1 hour and 1 second"
            elif day == 1 and hr == 1 and min == 1 and sec == 0:
                return "1 day, 1 hour and 1 minute"
            elif day == 1 and hr == 1 and min == 1 and sec == 1:
                return "1 day, 1 hour, 1 minute and 1 second"
            elif day == 1 and hr == 1 and min == 1 and sec > 1:
                return f"1 day, 1 hour, 1 minute and {sec} seconds"
            elif day == 1 and hr == 1 and min > 1 and sec == 0:
                return f"1 day, 1 hour and {min} minutes"
            elif day == 1 and hr == 1 and min > 1 and sec == 1:
                return f"1 day, 1 hour, {min} minutes and 1 second"
            elif day == 1 and hr == 1 and min > 1 and sec > 1:
                return f"1 day, 1 hour, {min} minutes and {sec} seconds"
            
            elif day == 1 and hr > 1 and min == 0 and sec == 0:
                return f"1 day and {hr} hours"
            elif day == 1 and hr > 1 and min == 0 and sec == 1:
                return f"1 day, {hr} hours and 1 second"
            elif day == 1 and hr > 1 and min == 1 and sec == 0:
                return f"1 day, {hr} hours and 1 minute"
            elif day == 1 and hr > 1 and min == 1 and sec == 1:
                return f"1 day, {hr} hours, 1 minute and 1 second"
            elif day == 1 and hr > 1 and min == 1 and sec > 1:
                return f"1 day, {hr} hours, 1 minute and {sec} seconds"
            elif day == 1 and hr > 1 and min > 1 and sec == 0:
                return f"1 day, {hr} hours and {min} minutes"
            elif day == 1 and hr > 1 and min > 1 and sec == 1:
                return f"1 day, {hr} hours, {min} minutes and 1 second"
            elif day == 1 and hr > 1 and min > 1 and sec > 1:
                return f"1 day, {hr} hours, {min} minutes and {sec} seconds"
            
            elif day > 1 and hr == 0 and min == 0 and sec == 0:
                return f"{day} days"
            elif day > 1 and hr == 0 and min == 0 and sec == 1:
                return f"{day} days and 1 second"
            elif day > 1 and hr == 0 and min == 1 and sec == 0:
                return f"{day} days and 1 minute"
            elif day > 1 and hr == 0 and min == 1 and sec == 1:
                return f"{day} days, 1 minute and 1 second"
            elif day > 1 and hr == 0 and min == 1 and sec > 1:
                return f"{day} days, 1 minute and {sec} seconds"
            elif day > 1 and hr == 0 and min > 1 and sec == 0:
                return f"{day} days and {min} minutes"
            elif day > 1 and hr == 0 and min > 1 and sec == 1:
                return f"{day} days, {min} minutes and 1 second"
            elif day > 1 and hr == 0 and min > 1 and sec > 1:
                return f"{day} days, {min} minutes and {sec} seconds"
            
            elif day > 1 and hr == 1 and min == 0 and sec == 0:
                return f"{day} days and 1 hour"
            elif day > 1 and hr == 1 and min == 0 and sec == 1:
                return f"{day} days, 1 hour and 1 second"
            elif day > 1 and hr == 1 and min == 1 and sec == 0:
                return f"{day} days, 1 hour and 1 minute"
            elif day > 1 and hr == 1 and min == 1 and sec == 1:
                return f"{day} days, 1 hour, 1 minute and 1 second"
            elif day > 1 and hr == 1 and min == 1 and sec > 1:
                return f"{day} days, 1 hour, 1 minute and {sec} seconds"
            elif day > 1 and hr == 1 and min > 1 and sec == 0:
                return f"{day} days, 1 hour and {min} minutes"
            elif day > 1 and hr == 1 and min > 1 and sec == 1:
                return f"{day} days, 1 hour, {min} minutes and 1 second"
            elif day > 1 and hr == 1 and min > 1 and sec > 1:
                return f"{day} days, 1 hour, {min} minutes and {sec} seconds"
                
            elif day > 1 and hr > 1 and min == 0 and sec == 0:
                return f"{day} days and {hr} hours"
            elif day > 1 and hr > 1 and min == 0 and sec == 1:
                return f"{day} days, {hr} hours and 1 second"
            elif day > 1 and hr > 1 and min == 1 and sec == 0:
                return f"{day} days, {hr} hours and 1 minute"
            elif day > 1 and hr > 1 and min == 1 and sec == 1:
                return f"{day} days, {hr} hours, 1 minute and 1 second"
            elif day > 1 and hr > 1 and min == 1 and sec > 1:
                return f"{day} days, {hr} hours, 1 minute and {sec} seconds"
            elif day > 1 and hr > 1 and min > 1 and sec == 0:
                return f"{day} days, {hr} hours and {min} minutes"
            elif day > 1 and hr > 1 and min > 1 and sec == 1:
                return f"{day} days, {hr} hours, {min} minutes and 1 second"
            elif day > 1 and hr > 1 and min > 1 and sec > 1:
                return f"{day} days, {hr} hours, {min} minutes and {sec} seconds"
            
        else:
            #years
            yr = seconds // 31536000
            rsec = seconds % 31536000
            day = rsec // 86400
            rsec2 = rsec % 86400
            hr = rsec2 // 3600
            rsec3 = rsec2 % 3600
            min = rsec3 // 60
            sec = rsec3 % 60
            
            # for year == 1
            if yr == 1 and day == 0 and hr == 0 and min == 0 and sec == 0:
                return "1 year"
            elif yr == 1 and day == 0 and hr == 0 and min == 0 and sec == 1:
                return "1 year and 1 second"
            elif yr == 1 and day == 0 and hr == 0 and min == 1 and sec == 0:
                return "1 year and 1 minute"
            elif yr == 1 and day == 0 and hr == 0 and min == 1 and sec == 1:
                return "1 year, 1 minute and 1 second"
            elif yr == 1 and day == 0 and hr == 0 and min > 1 and sec == 0:
                return f"1 year and {min} minutes"
            elif yr == 1 and day == 0 and hr == 0 and min > 1 and sec == 1:
                return f"1 year, {min} minutes and 1 second"
            elif yr == 1 and day == 0 and hr == 0 and min > 1 and sec > 1:
                return f"1 year, {min} minutes and {sec} seconds"
            
            elif yr == 1 and day == 0 and hr == 1 and min == 0 and sec == 0:
                return "1 year and 1 hour"
            elif yr == 1 and day == 0 and hr == 1 and min == 0 and sec == 1:
                return "1 year, 1 hour and 1 second"
            elif yr == 1 and day == 0 and hr == 1 and min == 1 and sec == 0:
                return "1 year, 1 hour and 1 minute"
            elif yr == 1 and day == 0 and hr == 1 and min == 1 and sec == 1:
                return "1 year, 1 hour, 1 minute and 1 second"
            elif yr == 1 and day == 0 and hr == 1 and min > 1 and sec == 0:
                return f"1 year, 1 hour and {min} minutes"
            elif yr == 1 and day == 0 and hr == 1 and min > 1 and sec == 1:
                return f"1 year, 1 hour, {min} minutes and 1 second"
            elif yr == 1 and day == 0 and hr == 1 and min > 1 and sec > 1:
                return f"1 year, 1 hour, {min} minutes and {sec} seconds"
            
            elif yr == 1 and day == 0 and hr > 1 and min == 0 and sec == 0:
                return f"1 year and {hr} hours"
            elif yr == 1 and day == 0 and hr > 1 and min == 0 and sec == 1:
                return f"1 year, {hr} hours and 1 second"
            elif yr == 1 and day == 0 and hr > 1 and min == 1 and sec == 0:
                return f"1 year, {hr} hours and 1 minute"
            elif yr == 1 and day == 0 and hr > 1 and min == 1 and sec == 1:
                return f"1 year, {hr} hours, 1 minute and 1 second"
            elif yr == 1 and day == 0 and hr > 1 and min > 1 and sec == 0:
                return f"1 year, {hr} hours and {min} minutes"
            elif yr == 1 and day == 0 and hr > 1 and min > 1 and sec == 1:
                return f"1 year, {hr} hours, {min} minutes and 1 second"
            elif yr == 1 and day == 0 and hr > 1 and min > 1 and sec > 1:
                return f"1 year, {hr} hours, {min} minutes and {sec} seconds"
            
            elif yr == 1 and day == 1 and hr == 0 and min == 0 and sec == 0:
                return "1 year and 1 day"
            elif yr == 1 and day == 1 and hr == 0 and min == 0 and sec == 1:
                return "1 year, 1 day and 1 second"
            elif yr == 1 and day == 1 and hr == 0 and min == 1 and sec == 0:
                return "1 year, 1 day and 1 minute"
            elif yr == 1 and day == 1 and hr == 0 and min == 1 and sec == 1:
                return "1 year, 1 day, 1 minute and 1 second"
            elif yr == 1 and day == 1 and hr == 0 and min > 1 and sec == 0:
                return f"1 year, 1 day and {min} minutes"
            elif yr == 1 and day == 1 and hr == 0 and min > 1 and sec == 1:
                return f"1 year, 1 day, {min} minutes and 1 second"
            elif yr == 1 and day == 1 and hr == 0 and min > 1 and sec > 1:
                return f"1 year, 1 day, {min} minutes and {sec} seconds"
            
            elif yr == 1 and day == 1 and hr == 1 and min == 0 and sec == 0:
                return "1 year, 1 day and 1 hour"
            elif yr == 1 and day == 1 and hr == 1 and min == 0 and sec == 1:
                return "1 year, 1 day, 1 hour and 1 second"
            elif yr == 1 and day == 1 and hr == 1 and min == 1 and sec == 0:
                return "1 year, 1 day, 1 hour and 1 minute"
            elif yr == 1 and day == 1 and hr == 1 and min == 1 and sec == 1:
                return "1 year, 1 day, 1 hour, 1 minute and 1 second"
            elif yr == 1 and day == 1 and hr == 1 and min > 1 and sec == 0:
                return f"1 year, 1 day, 1 hour and {min} minutes"
            elif yr == 1 and day == 1 and hr == 1 and min > 1 and sec == 1:
                return f"1 year, 1 day, 1 hour, {min} minutes and 1 second"
            elif yr == 1 and day == 1 and hr == 1 and min > 1 and sec > 1:
                return f"1 year, 1 day, 1 hour, {min} minutes and {sec} seconds"
            
            elif yr == 1 and day == 1 and hr > 1 and min == 0 and sec == 0:
                return f"1 year, 1 day and {hr} hours"
            elif yr == 1 and day == 1 and hr > 1 and min == 0 and sec == 1:
                return f"1 year, 1 day, {hr} hours and 1 second"
            elif yr == 1 and day == 1 and hr > 1 and min == 1 and sec == 0:
                return f"1 year, 1 day, {hr} hours and 1 minute"
            elif yr == 1 and day == 1 and hr > 1 and min == 1 and sec == 1:
                return f"1 year, 1 day, {hr} hours, 1 minute and 1 second"
            elif yr == 1 and day == 1 and hr > 1 and min > 1 and sec == 0:
                return f"1 year, 1 day, {hr} hours and {min} minutes"
            elif yr == 1 and day == 1 and hr > 1 and min > 1 and sec == 1:
                return f"1 year, 1 day, {hr} hours, {min} minutes and 1 second"
            elif yr == 1 and day == 1 and hr > 1 and min > 1 and sec > 1:
                return f"1 year, 1 day, {hr} hours, {min} minutes and {sec} seconds"
            
            elif yr == 1 and day > 1 and hr == 0 and min == 0 and sec == 0:
                return f"1 year and {day} days"
            elif yr == 1 and day > 1 and hr == 0 and min == 0 and sec == 1:
                return f"1 year, {day} days and 1 second"
            elif yr == 1 and day > 1 and hr == 0 and min == 1 and sec == 0:
                return f"1 year, {day} days and 1 minute"
            elif yr == 1 and day > 1 and hr == 0 and min == 1 and sec == 1:
                return f"1 year, {day} days, 1 minute and 1 second"
            elif yr == 1 and day > 1 and hr == 0 and min > 1 and sec == 0:
                return f"1 year, {day} days and {min} minutes"
            elif yr == 1 and day > 1 and hr == 0 and min > 1 and sec == 1:
                return f"1 year, {day} days, {min} minutes and 1 second"
            elif yr == 1 and day > 1 and hr == 0 and min > 1 and sec > 1:
                return f"1 year, {day} days, {min} minutes and {sec} seconds"
            
            elif yr == 1 and day > 1 and hr == 1 and min == 0 and sec == 0:
                return f"1 year, {day} days and 1 hour"
            elif yr == 1 and day > 1 and hr == 1 and min == 0 and sec == 1:
                return f"1 year, {day} days, 1 hour and 1 second"
            elif yr == 1 and day > 1 and hr == 1 and min == 1 and sec == 0:
                return f"1 year, {day} days, 1 hour and 1 minute"
            elif yr == 1 and day > 1 and hr == 1 and min == 1 and sec == 1:
                return f"1 year, {day} days, 1 hour, 1 minute and 1 second"
            elif yr == 1 and day > 1 and hr == 1 and min > 1 and sec == 0:
                return f"1 year, {day} days, 1 hour and {min} minutes"
            elif yr == 1 and day > 1 and hr == 1 and min > 1 and sec == 1:
                return f"1 year, {day} days, 1 hour, {min} minutes and 1 second"
            elif yr == 1 and day > 1 and hr == 1 and min > 1 and sec > 1:
                return f"1 year, {day} days, 1 hour, {min} minutes and {sec} seconds"
                
            elif yr == 1 and day > 1 and hr > 1 and min == 0 and sec == 0:
                return f"1 year, {day} days and {hr} hours"
            elif yr == 1 and day > 1 and hr > 1 and min == 0 and sec == 1:
                return f"1 year, {day} days, {hr} hours and 1 second"
            elif yr == 1 and day > 1 and hr > 1 and min == 1 and sec == 0:
                return f"1 year, {day} days, {hr} hours and 1 minute"
            elif yr == 1 and day > 1 and hr > 1 and min == 1 and sec == 1:
                return f"1 year, {day} days, {hr} hours, 1 minute and 1 second"
            elif yr == 1 and day > 1 and hr > 1 and min > 1 and sec == 0:
                return f"1 year, {day} days, {hr} hours and {min} minutes"
            elif yr == 1 and day > 1 and hr > 1 and min > 1 and sec == 1:
                return f"1 year, {day} days, {hr} hours, {min} minutes and 1 second"
            elif yr == 1 and day > 1 and hr > 1 and min > 1 and sec > 1:
                return f"1 year, {day} days, {hr} hours, {min} minutes and {sec} seconds"
            
            # for year > 1
            elif yr > 1 and day == 0 and hr == 0 and min == 0 and sec == 0:
                return f"{yr} years"
            elif yr > 1 and day == 0 and hr == 0 and min == 0 and sec == 1:
                return f"{yr} years and 1 second"
            elif yr > 1 and day == 0 and hr == 0 and min == 1 and sec == 0:
                return f"{yr} years and 1 minute"
            elif yr > 1 and day == 0 and hr == 0 and min == 1 and sec == 1:
                return f"{yr} years, 1 minute and 1 second"
            elif yr > 1 and day == 0 and hr == 0 and min > 1 and sec == 0:
                return f"{yr} years and {min} minutes"
            elif yr > 1 and day == 0 and hr == 0 and min > 1 and sec == 1:
                return f"{yr} years, {min} minutes and 1 second"
            elif yr > 1 and day == 0 and hr == 0 and min > 1 and sec > 1:
                return f"{yr} years, {min} minutes and {sec} seconds"
            
            elif yr > 1 and day == 0 and hr == 1 and min == 0 and sec == 0:
                return f"{yr} years and 1 hour"
            elif yr > 1 and day == 0 and hr == 1 and min == 0 and sec == 1:
                return f"{yr} years, 1 hour and 1 second"
            elif yr > 1 and day == 0 and hr == 1 and min == 1 and sec == 0:
                return f"{yr} years, 1 hour and 1 minute"
            elif yr > 1 and day == 0 and hr == 1 and min == 1 and sec == 1:
                return f"{yr} years, 1 hour, 1 minute and 1 second"
            elif yr > 1 and day == 0 and hr == 1 and min > 1 and sec == 0:
                return f"{yr} years, 1 hour and {min} minutes"
            elif yr > 1 and day == 0 and hr == 1 and min > 1 and sec == 1:
                return f"{yr} years, 1 hour, {min} minutes and 1 second"
            elif yr > 1 and day == 0 and hr == 1 and min > 1 and sec > 1:
                return f"{yr} years, 1 hour, {min} minutes and {sec} seconds"
            
            elif yr > 1 and day == 0 and hr > 1 and min == 0 and sec == 0:
                return f"{yr} years and {hr} hours"
            elif yr > 1 and day == 0 and hr > 1 and min == 0 and sec == 1:
                return f"{yr} years, {hr} hours and 1 second"
            elif yr > 1 and day == 0 and hr > 1 and min == 1 and sec == 0:
                return f"{yr} years, {hr} hours and 1 minute"
            elif yr > 1 and day == 0 and hr > 1 and min == 1 and sec == 1:
                return f"{yr} years, {hr} hours, 1 minute and 1 second"
            elif yr > 1 and day == 0 and hr > 1 and min > 1 and sec == 0:
                return f"{yr} years, {hr} hours and {min} minutes"
            elif yr > 1 and day == 0 and hr > 1 and min > 1 and sec == 1:
                return f"{yr} years, {hr} hours, {min} minutes and 1 second"
            elif yr > 1 and day == 0 and hr > 1 and min > 1 and sec > 1:
                return f"{yr} years, {hr} hours, {min} minutes and {sec} seconds"
            
            elif yr > 1 and day == 1 and hr == 0 and min == 0 and sec == 0:
                return f"{yr} years and 1 day"
            elif yr > 1 and day == 1 and hr == 0 and min == 0 and sec == 1:
                return f"{yr} year, 1 day and 1 second"
            elif yr > 1 and day == 1 and hr == 0 and min == 1 and sec == 0:
                return f"{yr} years, 1 day and 1 minute"
            elif yr > 1 and day == 1 and hr == 0 and min == 1 and sec == 1:
                return f"{yr} years, 1 day, 1 minute and 1 second"
            elif yr > 1 and day == 1 and hr == 0 and min > 1 and sec == 0:
                return f"{yr} years, 1 day and {min} minutes"
            elif yr > 1 and day == 1 and hr == 0 and min > 1 and sec == 1:
                return f"{yr} years, 1 day, {min} minutes and 1 second"
            elif yr > 1 and day == 1 and hr == 0 and min > 1 and sec > 1:
                return f"{yr} years, 1 day, {min} minutes and {sec} seconds"
            
            elif yr > 1 and day == 1 and hr == 1 and min == 0 and sec == 0:
                return f"{yr} years, 1 day and 1 hour"
            elif yr > 1 and day == 1 and hr == 1 and min == 0 and sec == 1:
                return f"{yr} years, 1 day, 1 hour and 1 second"
            elif yr > 1 and day == 1 and hr == 1 and min == 1 and sec == 0:
                return f"{yr} years, 1 day, 1 hour and 1 minute"
            elif yr > 1 and day == 1 and hr == 1 and min == 1 and sec == 1:
                return f"{yr} years, 1 day, 1 hour, 1 minute and 1 second"
            elif yr > 1 and day == 1 and hr == 1 and min > 1 and sec == 0:
                return f"{yr} years, 1 day, 1 hour and {min} minutes"
            elif yr > 1 and day == 1 and hr == 1 and min > 1 and sec == 1:
                return f"{yr} years, 1 day, 1 hour, {min} minutes and 1 second"
            elif yr > 1 and day == 1 and hr == 1 and min > 1 and sec > 1:
                return f"{yr} years, 1 day, 1 hour, {min} minutes and {sec} seconds"
            
            elif yr > 1 and day == 1 and hr > 1 and min == 0 and sec == 0:
                return f"{yr} years, 1 day and {hr} hours"
            elif yr > 1 and day == 1 and hr > 1 and min == 0 and sec == 1:
                return f"{yr} years, 1 day, {hr} hours and 1 second"
            elif yr > 1 and day == 1 and hr > 1 and min == 1 and sec == 0:
                return f"{yr} years, 1 day, {hr} hours and 1 minute"
            elif yr > 1 and day == 1 and hr > 1 and min == 1 and sec == 1:
                return f"{yr} years, 1 day, {hr} hours, 1 minute and 1 second"
            elif yr > 1 and day == 1 and hr > 1 and min > 1 and sec == 0:
                return f"{yr} years, 1 day, {hr} hours and {min} minutes"
            elif yr > 1 and day == 1 and hr > 1 and min > 1 and sec == 1:
                return f"{yr} years, 1 day, {hr} hours, {min} minutes and 1 second"
            elif yr > 1 and day == 1 and hr > 1 and min > 1 and sec > 1:
                return f"{yr} years, 1 day, {hr} hours, {min} minutes and {sec} seconds"
            
            elif yr > 1 and day > 1 and hr == 0 and min == 0 and sec == 0:
                return f"{yr} years and {day} days"
            elif yr > 1 and day > 1 and hr == 0 and min == 0 and sec == 1:
                return f"{yr} years, {day} days and 1 second"
            elif yr > 1 and day > 1 and hr == 0 and min == 1 and sec == 0:
                return f"{yr} years, {day} days and 1 minute"
            elif yr > 1 and day > 1 and hr == 0 and min == 1 and sec == 1:
                return f"{yr} years, {day} days, 1 minute and 1 second"
            elif yr > 1 and day > 1 and hr == 0 and min > 1 and sec == 0:
                return f"{yr} years, {day} days and {min} minutes"
            elif yr > 1 and day > 1 and hr == 0 and min > 1 and sec == 1:
                return f"{yr} years, {day} days, {min} minutes and 1 second"
            elif yr > 1 and day > 1 and hr == 0 and min > 1 and sec > 1:
                return f"{yr} years, {day} days, {min} minutes and {sec} seconds"
            
            elif yr > 1 and day > 1 and hr == 1 and min == 0 and sec == 0:
                return f"{yr} years, {day} days and 1 hour"
            elif yr > 1 and day > 1 and hr == 1 and min == 0 and sec == 1:
                return f"{yr} years, {day} days, 1 hour and 1 second"
            elif yr > 1 and day > 1 and hr == 1 and min == 1 and sec == 0:
                return f"{yr} years, {day} days, 1 hour and 1 minute"
            elif yr > 1 and day > 1 and hr == 1 and min == 1 and sec == 1:
                return f"{yr} years, {day} days, 1 hour, 1 minute and 1 second"
            elif yr > 1 and day > 1 and hr == 1 and min > 1 and sec == 0:
                return f"{yr} years, {day} days, 1 hour and {min} minutes"
            elif yr > 1 and day > 1 and hr == 1 and min > 1 and sec == 1:
                return f"{yr} years, {day} days, 1 hour, {min} minutes and 1 second"
            elif yr > 1 and day > 1 and hr == 1 and min > 1 and sec > 1:
                return f"{yr} years, {day} days, 1 hour, {min} minutes and {sec} seconds"
                
            elif yr > 1 and day > 1 and hr > 1 and min == 0 and sec == 0:
                return f"{yr} years, {day} days and {hr} hours"
            elif yr > 1 and day > 1 and hr > 1 and min == 0 and sec == 1:
                return f"{yr} years, {day} days, {hr} hours and 1 second"
            elif yr > 1 and day > 1 and hr > 1 and min == 1 and sec == 0:
                return f"{yr} years, {day} days, {hr} hours and 1 minute"
            elif yr > 1 and day > 1 and hr > 1 and min == 1 and sec == 1:
                return f"{yr} years, {day} days, {hr} hours, 1 minute and 1 second"
            elif yr > 1 and day > 1 and hr > 1 and min > 1 and sec == 0:
                return f"{yr} years, {day} days, {hr} hours and {min} minutes"
            elif yr > 1 and day > 1 and hr > 1 and min > 1 and sec == 1:
                return f"{yr} years, {day} days, {hr} hours, {min} minutes and 1 second"
            elif yr > 1 and day > 1 and hr > 1 and min > 1 and sec > 1:
                return f"{yr} years, {day} days, {hr} hours, {min} minutes and {sec} seconds"

    return "Invalid input"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./humanClock.py <integer>")
        sys.exit(1)
    
    try:
        seconds = int(sys.argv[1])
        result = format_duration(seconds)
        print(result)  # Logs the result to Bash terminal
    except ValueError:
        print("Usage: ./humanClock.py <integer>")
        sys.exit(1)