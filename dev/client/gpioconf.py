import json

gpioconfig=json.dumps(
    [
        {
            "type": "title",
            "title": "P17"
        },
        {
            "type": "options",
            "title": "Mode",
            "desc": "there 2 modes, GPIO.OUT or GPIO.IN",
            "section": "P17",
            "options": ["GPIO.IN","GPIO.OUT"],
            "key": "p17mode"
        },
        {
            "type" : "bool",
            "title" : "State",
            "desc" : "The default is OFF",
            "section" : "P17",
            "key" : "p17state"
        },
        {
            "type": "bool",
            "title": "PWM",
            "desc": "Pulse with modulation, mode must be GPIO.OUT",
            "section" : "P17",
            "key" : "p17pwm"
        },
        {
            "type": "numeric",
            "title": "Frequencies",
            "desc": "range between 1 - 10000 Hz",
            "section" : "P17",
            "key" : "p17freq"
        },
        {
            "type": "numeric",
            "title": "Duty Cycle",
            "desc": "value in percent between 1 - 100",
            "section" : "P17",
            "key" : "p17dc"
        },

        {
            "type": "title",
            "title": "P18"
        },
        {
            "type": "options",
            "title": "Mode",
            "desc": "there 2 modes, GPIO.OUT or GPIO.IN",
            "section": "P18",
            "options": ["GPIO.IN","GPIO.OUT"],
            "key": "p18mode"
        },
        {
            "type" : "bool",
            "title" : "State",
            "desc" : "The default is OFF",
            "section" : "P18",
            "key" : "p18state"
        },
        {
            "type": "bool",
            "title": "PWM",
            "desc": "Pulse with modulation, mode must be GPIO.OUT",
            "section" : "P18",
            "key" : "p18pwm"
        },
        {
            "type": "numeric",
            "title": "Frequencies",
            "desc": "range between 1 - 10000 Hz",
            "section" : "P18",
            "key" : "p18freq"
        },
        {
            "type": "numeric",
            "title": "Duty Cycle",
            "desc": "value in percent between 1 - 100",
            "section" : "P18",
            "key" : "p18dc"
        }
    ]
)