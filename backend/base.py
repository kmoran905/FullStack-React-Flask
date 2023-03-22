from flask import Flask, url_for

api = Flask(__name__)

@api.route('/profile')
def my_profile():
    response_body = {
        "profiles": [{
        
        "id": "1",
        "name": "Nagato Uzumaki",
        "about" :"a shinobi of Amegakure and descendant of the Uzumaki clan. Forming Akatsuki alongside his friends (and fellow war orphans) Yahiko and Konan, Nagato dreamed of bringing peace to the violent shinobi world. However, following Yahiko's death, Nagato adopted the alias of Pain (ペイン, Pein) and, along with Konan, began leading a new Akatsuki — one that would force the world into peace using any means necessary",
        "image" : "/static/nagato.jpeg",
        },

        {
        "id" : "2",
        "name": "Isshiki Ōtsutsuki",
        "about": "was a member of the Ōtsutsuki clan's main family who originally came to Earth with Kaguya to plant a God Tree and harvest its chakra fruit. He was betrayed by Kaguya, who left him for dead, and took over the body of a novice monk named Jigen, ",
        "image": "/static/isshiki.jpeg",

        },

        {
        "id" : "3",
        "name": "Momoshiki Ōtsutsuki",
        "about": "Was a member of the Ōtsutsuki clan's main family, sent to investigate the whereabouts of Kaguya and her God Tree and then attempting to cultivate a new one out of the chakra of the Seventh Hokage.",
        "image": "/static/momoshiki.jpeg",
        
        },
        
        {
        "id" : "4",
        "name": "Madara Uchiha",
        "about": "was the legendary leader of the Uchiha Clan. He founded Konohagakure alongside his childhood friend and rival, Hashirama Senju, with the intention of bringing about an era of peace. When the two couldn't agree on how to achieve that peace, they fought for control of the village, a conflict which ended in Madara's death. Madara.",
        "image": "/static/madara.jpeg",
        


        }]
    }

    return response_body

with api.test_request_context():
    print(url_for('my_profile'))

