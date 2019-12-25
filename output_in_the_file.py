def setTitle(title):
    return f"Title: {title}"


def setTarget(targetEmail):
    return f"mailto:{targetEmail}"


def prepareMail(name, target, title, date, subject):
    message = f"""
    
    {setTitle(title)}
    
    {setTarget(target)}
    
    Date : {date}
    Subject : {subject} 
    
    Hello {name},
        I have been working on the AI Bot I belive 
        You have been working in the industry from 
        long time can you please suggest me something 
        that can workout for me.
                        
        hope, you have been doing well 
                        
        Warm Regard,
                            
        Ajay Sharma
        System Engineer 
        Google , Seatle
        US
        """
    return message


name = input("Enter Name Of Reciver : ")
email = input("Enter Email Id : ")
title = input("Enter Title : ")
subject = input("Enter Subject : ")
date = input("Enter date : ")


file = open(f"mail.txt", "w")
file.write(prepareMail(name, email, title, date, subject))
