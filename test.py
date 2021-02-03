from google_trans_new import google_translator
source=""" China hosted the 2008 Summer Olympics in Beijing, where its athletes received 51 gold medals – the highest number of gold medals of any participating nation that year.
 China also won the most medals of any nation at the 2012 Summer Paralympics, with 231 overall, including 95 gold medals.
 In 2011, Shenzhen in Guangdong, China hosted the 2011 Summer Universiade.
 China hosted the 2013 East Asian Games in Tianjin and the 2014 Summer Youth Olympics in Nanjing; the first country to host both regular and Youth Olympics.
 Beijing and its nearby city Zhangjiakou of Hebei province will also collaboratively host the 2022 Olympic Winter Games, which will make Beijing the first city in the world to hold both the Summer Olympics and the Winter Olympics."""
translator = google_translator()  
translate_text = translator.translate(source,lang_tgt='zh')
print(translate_text)

