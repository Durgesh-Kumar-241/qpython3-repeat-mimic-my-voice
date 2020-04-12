
"""
License

Copyright (c) <year> <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

__author__="Durgesh kumar,MNNIT ALLAHABD"
__copyright__="all rights reserved"
"""copy / mimic user voice """
""" use with internet for better experiance"""

import androidhelper
import time
droid = androidhelper.Android()
droid.makeToast("Welcome")
def listen(): 
    global result,error
  
    x, result, error = droid.recognizeSpeech("jarvis command") 
    
    result = result.lower()
    droid.makeToast(result)





while True:
    res, relt, ser = droid.ttsIsSpeaking()
    if relt is False:   
        listen()

        if(len(str(result))>0):
            if(result=="exit"):
                break
            else:
            
                droid.ttsSpeak(result)
                
    else:
        time.sleep(.1)               
