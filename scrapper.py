import bs4 as bs
import urllib.request

url_num = int(input("Enter Url Number ...Example http://gtu-mcq.com/BE/Computer-Engineering/Semester-8/2180703/5161/MCQs?q=9aZHDjblmRk= ......In my case it is 5161 :  "))
sub_code = input("Enter Subject code...Example 2180703 : ")
total_units = int(input("Enter number of units...Example 8 : "))
branch = input("Enter branch...Example(Computer, Mechanical, Electrical..enter in same format) : ")
semester = input("Enter semester...Example 8 : ")

pagination = ["9aZHDjblmRk", "bDFvcmdllQA", "6wHWymi73nk", "62pxAP7c7zo" , "F/I0jXYbK4A" , "V5gItqXdDZ0", "/a8zqq5LsNk", "PiCGJToqDwo", "013G9Ftq0lc", "w7DGoNvS53U", "3250OxRQXCo", "RyBhlP9tjis", "31WIp9duVMU", "WwctbSKBVt4", "zoLCy/Hv7S4", "mwHzaMDbcic", "Yc4Re0O6m3E"]
print(len(pagination))

total_pages = url_num + int(total_units) + 5

while True:
    print(url_num)
    if url_num == total_pages:
        break
    for page in pagination:
        try :
            source = urllib.request.urlopen('http://gtu-mcq.com/BE/{}-Engineering/Semester-{}/{}/{}/MCQs?q={}='.format(branch,semester,str(sub_code),str(url_num),page)).read()
        except :
            break

        soup = bs.BeautifulSoup(source,'lxml')

        # question_elements = soup.findAll("td", {'class':'td-q'})
        question_elements = soup.findAll("div", {'class':'form-group div-question g-font-size-15'})
        if len(question_elements) == 0 or question_elements == None:
            break

        file1 = open("Questions.txt","a", encoding='utf-8')

        for q_element in question_elements:
            file1.write("Question : " + q_element.find("div", {'class':'g-font-weight-600'}).text.strip() + '\n')
            options_table = q_element.findAll("table")[1]
            option_table = options_table.findAll("td")
            for i in range(0,len(option_table),2):
                file1.write(option_table[i].text.strip() + ' ' + option_table[i+1].text.strip() + '\n')
            answer = q_element.find("div", {'class':'col'})
            file1.write("Option" + answer.find("b").text.strip() + '\n\n')
    url_num += 1

print("Hurray!!! Scrapping Completed, Check the Question.txt file")