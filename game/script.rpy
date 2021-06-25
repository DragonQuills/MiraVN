################################################################################
## Initialization
################################################################################

# The menu has two options - "char" and "v"
# v is the basic vertical menu. "char" is a spread out horizontal menu only used on the character selection screen
default menu_style = "v"

transform center_right:
    xalign 0.35
    yalign 1.0

transform center_right:
    xalign 0.60
    yalign 1.0

################################################################################
## Character Definitions
################################################################################

define m = Character("Mira", color = "#F6AEA0")
define mc = Character("[name]", image = "mc",  color = "#6db0eb")


################################################################################
## Images
################################################################################
# Define Mira images
image mira sad = im.FactorScale("images/mira/mira sad.png", 0.6)
image mira little sad = im.FactorScale("images/mira/mira little sad.png", 0.6)
image mira happy = im.FactorScale("images/mira/mira happy.png", 0.6)
image mira shocked = im.FactorScale("images/mira/mira shocked.png", 0.6)
image mira normal = im.FactorScale("images/mira/mira normal.png", 0.6)
image mira angry = im.FactorScale("images/mira/mira angry.png", 0.6)
image mira annoyed = im.FactorScale("images/mira/mira annoyed.png", 0.6)
image mira delighted = im.FactorScale("images/mira/mira delighted.png", 0.6)
image mira smug = im.FactorScale("images/mira/mira smug.png", 0.6)

# Define images for the character picker screen
image char1 andro fem = im.FactorScale("images/mc/char1 andro fem.png", 0.4)
image char2 andro masc = im.FactorScale("images/mc/char2 andro masc.png", 0.4)
image char3 fem = im.FactorScale("images/mc/char3 fem.png", 0.4)
image char4 masc = im.FactorScale("images/mc/char4 masc.png", 0.4)

# Set up MC images
default mc_type = "andro_masc"

# used to position the mc at the lower left corner of the screen at a small size
transform mc_transform:
    xalign -0.1
    zoom 0.3

# The DynamicImage lets me do string interpolation of mc_type to let the player pick their character
# the At(imagelike, transformations) lets me apply the position and zoom as defaults
# "side" is useds to mark that the image should be a mini image on the side of the screen above the text box
image side mc smile = At(DynamicImage("images/mc/[mc_type]/smile.png"), mc_transform)
image side mc shocked = At(DynamicImage("images/mc/[mc_type]/shocked.png"), mc_transform)
image side mc delighted = At(DynamicImage("images/mc/[mc_type]/delighted.png"), mc_transform)
image side mc happy = At(DynamicImage("images/mc/[mc_type]/happy.png"), mc_transform)
image side mc angry = At(DynamicImage("images/mc/[mc_type]/angry.png"), mc_transform)
image side mc annoyed = At(DynamicImage("images/mc/[mc_type]/annoyed.png"), mc_transform)
image side mc sad = At(DynamicImage("images/mc/[mc_type]/sad.png"), mc_transform)
image side mc little sad = At(DynamicImage("images/mc/[mc_type]/little sad.png"), mc_transform)
image side mc smug = At(DynamicImage("images/mc/[mc_type]/smug.png"), mc_transform)

image mc smile = At(DynamicImage("images/mc/[mc_type]/smile.png"), mc_transform)

default pronouns = "they"
default pronouns_type = "plural"

image grey cat flop = im.FactorScale("images/cats/grey-kitten/grey-kitten2.png", 0.6)
image grey cat sleep = im.FactorScale("images/cats/grey-kitten/grey-kitten4.png", 0.6)
image white cat curl = im.FactorScale("images/cats/white-kitten/white-kitten8.png", 0.6)

################################################################################
## Game
################################################################################

label start:
    transform center_right:
        xalign 0.35
        yalign 1.0

    transform center_right:
        xalign 0.60
        yalign 1.0

    label setup:
        scene bg blue

        python:
            name = renpy.input("What's your name?")

            name = name.strip() or ("Kayden")

            # how much Mira likes the MC.
            # Needs to be above something for dating or strong friendship
            # If too low, MC and Mira will drift apart.
            # 100 is the highest the affection can get, 0 is the lowest
            affection = 50

        # Display characters for character picker
        show char1 andro fem:
            xalign -0.10
            yalign 1.0

        show char2 andro masc:
            xalign 0.25
            yalign 1.0

        show char3 fem:
            xalign 0.70
            yalign 1.0

        show char4 masc:
            xalign 1.1
            yalign 1.0


        $ menu_style = "char"

        # TODO: put this stuff in the gui or screen file somehow, it shouldn't be here.
        # default gui.choice_button_width = 300

        # TODO: reset the menu type and the gui button width after this menu.

        menu:
            "Pick what you want to look like."

            "Definitely this cutie!":
                $ mc_type = "andro_fem"
                
            "No, this lil darling!":
                $ mc_type = "andro_masc"

            "Wait no, this sweetie!":
                $ mc_type = "fem"
            
            "Final answer, this bae!":
                $ mc_type = "masc"
        
        $ menu_style = "v"
        # $ gui.choice_button_width = 790

        # pick pronouns!
        menu:
            "Which pronouns would you like your character to use?"

            "they/them":
                $ pronouns = "they"
                $ pronouns_type = "plural"
            "she/her":
                $ pronouns = "she"
                $ pronouns_type = "sing"
            "he/him":
                $ pronouns = "he"
                $ pronouns_type = "sing"

        label are_you_sure_setup:
            hide char1
            hide char2
            hide char3
            hide char4
            
            show mc smile:
                xalign 0.5
                yalign 1.0
                zoom 1.5
            menu:
                "Name: [name] \nPronouns: [pronouns] \nIs this correct?"

                "Yes!":
                    jump park_intro
                "No...":
                    jump setup


    label park_intro:
        scene bg park
        with Dissolve(1)

        play music "audio/music/peaceful.mp3" fadein 2

        pause(0.5)

        "I waited on the bench patiently, even though Mira was already half-an-hour late."

        "Well, \"patiently\" might have been giving me too much credit - Mira had a habit of running late, no matter how much I nagged her about it."

        "Still, half-an-hour was pushing it, even for her..."

        "Well, at least it was a nice day to be kept waiting."

        "The sunlight made a mosaic out of the freshly fallen autumn leaves and the cool breeze coming off of the lake felt nice on my skin."

        "Fall had always been my favorite season. Something about the feeling of change in the air was somehow exhilarating yet peaceful to me."

        "This year was particularly beautiful. Every tree seemed to be trying to outshine all the others with dazzling colors. There was a faint scent of maple in the air and the only sound was the quiet breeze as it rustled the leaves."

        "Though the day would be a bit nicer if {i}someone{/i} would show up even remotely on time..."

        "I checked my watch. Almost forty minutes late. Where was she...?"

        show mira sad at right
        with moveinright

        "Just as I was beginning to get worried, I saw Mira racing towards me, a paper bag clutched in her hand."

        m "Ahhhhh I'm sorry I'm late again!!!"

        "Mira charged over to me and flung her arms around me in a tight hug. She always smelled a little bit like pumpkin spice during autumn and today was no exception."

        m "Please please please don't be upset, I promise there's a good reason!"

        "I sighed and ran my finger through my hair."

        mc annoyed "Fine, fine, what's the reason?"

        show mira normal

        "Mira's face brightened and she pulled back from the hug then proudly displayed her paper bag."

        show mira happy
        m "This is the reason!"

        "I decided to give Mira a little bit of a hard time for keeping me waiting so long."

        mc annoyed "A... paper bag is the reason I've been sitting here for the better part of an hour?"

        show mira annoyed
        m "No, of course not!"

        "My stern facade broke at her indignant face and I couldn't help but laugh. It was impossible to stay angry at Mira when she pouted like that."

        mc delighted "Sorry, Mira. What's in the bag?"

        show mira normal
        m "Ok, sooooo, you know that new pastry store that opened downtown?"

        mc shocked"The one run by some famous chef from France?"

        m "Yup! Well, today they were having a special deal - buy-one-get-one-free! So I got us some!"

        "Mira opened up the bag and pulled out two decedent looking pastries then offered one to me."

        show mira delighted
        m "See? I told you I had a good reason!"

        mc smile "That you did."

        "I moved over, making space on the bench for Mira to sit down with me."

        scene bg bench
        with Dissolve(1.0)

        show mira normal at right
        with Dissolve(1.0)

        "Mira plopped down on the bench and rested her head against my shoulder."

        "We sat in the quiet of the park for a while, just eating our pastries and enjoying each other's company."

        "Mira chewed her pastry slowly, enjoying every bite of it, so she still had half of hers left by the time I finished mine."

        menu:
            "I decided to..."

            "Steal her pastry!":
                jump steal_pastry
            "Ask for a bite.":
                jump ask_for_bite
            "Just relax and enjoy the day.":
                jump relax

        label steal_pastry:

            "I reached out and snagged Mira's pastry right from her unsuspecting hands."

            show mira shocked
            m "Hey! [name]! Give that back!"

            mc smug"Never! Pastries or death!"

            show mira sad
            m "C'mon, [name], please..."

            "Mira turned the full force of her sad puppy-dog eyes towards me."

            m "You know chocolate's my favorite flavor..."

            menu:
                "Give it back.":
                    jump give_back
                "Stuff the whole thing in your mouth.":
                    jump eat_it

            label give_back:
                $ affection += 10

                mc smile "Fiiiiine."

                show mira delighted
                "I handed Mira her pastry back and she beamed."

                m "And now for your delicious reward..."

                jump more_pastries

            label eat_it:
                $ affection -= 10
                show mira shocked
                "I watched Mira's look of horror as I crammed the entire pastry into my mouth."

                show mira angry
                m "[name], you jerk!"

                m "Well fine, I guess I'll have to eat the rest of them by myself then!"

                "I swallowed the pastry, then looked at Mira in surprise."

                mc shocked "Wait, there were more?"

                m "Of course, you think I would keep you waiting for an hour for a single pastry?"


                m "But now they're all mine, you butt!"

                show mira smug
                "Mira ate several more pastries in front of me painfully slowly. She watched me with a smug expression to make sure I didn't steal any more."

                jump leaving_park


        label ask_for_bite:
            $ affection += 10

            mc little sad "Could I have a bite?"

            "Mira looked up at me from my shoulder."

            show mira delighted
            m "I can do you one better!"

            jump more_pastries

        label relax:
            $ affection += 5

            "I leaned back and enjoyed the feelings of the sunlight on my face and Mira resting on my shoulder."

            "After a while of resting, Mira sat up."
            show mira normal
            m "Hey, guess what?"

            mc smile "Hmm?"

            jump more_pastries


        label more_pastries:
            m "I bought more pastries!"

            hide mira
            with Dissolve(0.8)

            show mira delighted at right
            with Dissolve(0.5)

            "Mira ducked down and grabbed two more pastries from the paper bag at our feet."

            "She offered me an orange Danish and sat back down to what looked like a raspberry croissant."

            m "Thanks for eating the orange ones! I don't like them, too bitter for me."

            mc happy "No problem, I don't mind them."

            "We ate our pastries together and relaxed, soaking up the sun and each other's company."

            jump leaving_park

        label leaving_park:

            scene bg black
            with Dissolve(1)

            scene bg bench
            with Dissolve(1)
            show mira normal at right
            with Dissolve(0.3)

            "After a while, Mira stood up abruptly and dusted the crumbs off of her jeans."

            m "Well, it's about time for me to head home. Are we still on for tomorrow?"

            "Oh, right. I had agreed to meet Mira at our favorite cafe - a place with delicious drinks, tasty food, and best of all..."

            show bg hearts_and_cats
            hide mira

            "CATS!"

            "Such adorable little furballs, I couldn't help but love them. The cafe had between three and a dozen cats at a time, most of which were up for adoption. Mira loved cats as much as I did so we went to the cafe together at least once a week."

            "Unfortunately, Mira's apartment wasn't pet-friendly, or she definitely would have adopted one. Although maybe that was a good thing - I had talked Mira out of getting a cat more times than I could count."

            "If she got a pet-friendly apartment she might suffocate under the weight of cat hair from the 30 cats she would adopt. Or at least go broke from buying premium pet food for them."

            show bg park
            with Dissolve(0.5)
            show mira normal

            menu:
                "Mira was still waiting on my answer."

                "I'll definitely be there!":
                    $ cafe_eww = False
                    jump cafe_yes
                "Ugh, but 10am is so early... If I have to...":
                    $ cafe_eww = True
                    jump cafe_eww

            label cafe_yes:
                $ affection += 10

                show mira delighted

                "Mira grinned from ear-to-ear."

                m "Great! Well, I'll see you there!"

                jump end_day

            label cafe_eww:
                $ affection -=10

                show mira sad

                "Mira frowned at me and folded her arms uncomfortably."

                m "I mean, of course you don't have to come if you don't want to, it's just our regular thing, so..."

                mc little sad "Nah, I guess it's fine. I'll see you there."

                m "Ok, if you're sure..."

                jump end_day

        label end_day:
            # fix that!
            "I said goodbye to Mira and started to walk back to my apartment."

            show mira happy

            m "Remember, 10am sharp! If you're late you have to buy the drinks and snacks."

            mc smug "Yeah right, as if you're going to get there earlier than I am, Ms. Hour Late!"

            show mira annoyed
            "Mira stuck out her tongue at me and we both went our separate ways."
            hide mira
            with easeoutright

            scene bg park night
            with Dissolve(2)
            play music "audio/music/night.mp3" fadeout 1 fadein 1

            "I walked back to my apartment as night blanketed the town around me. The moon and fireflies provided light where the streetlights couldn't reach, dusting the world with a gentle glow that softened the shadows."
            "The air turned from the crisp of autumn days to the cold of autumn nights and I was grateful for my scarf as the air nipped at my face. I breathed in the scent of incoming rain and increased my pace."

            scene bg moon
            with Dissolve(1)
            "As I was about to exit the park, I slowed and looked up at the moon and thought about my day with Mira."
            "Mira and I had been friends for quite some time now and we'd grown comfortable with each other."

            menu:
                "But did I want our relationship to change?"

                "No, I like our friendship and don't want to change it.":
                    $ date = False
                    jump walk_home
                "Yes, I'm interested in a romantic relationship with Mira.":
                    $ date = True
                    jump walk_home
                    
        label walk_home:
            scene bg city night
            with Dissolve(1)
            "I left the park and moved to the streets, keeping a swifter pace to avoid the rain."
            "Fortunately I made it home right in time, arriving at my apartment right as the pitter-patter of light rain began."

            scene bg bedroom:
                zoom 0.4
            with Dissolve(0.5)
            "I stepped inside, removed my outerwear, and went to my bedroom to change into my pajamas. I was tired from the long day and I soon entered the strange state between wakefulness and sleep."
            if date:
                "I thought about how to ask Mira if she felt the same as I drifted into a peaceful sleep..."
            else:
                "I thought about how happy I was to have Mira in my life  as I drifted into a peaceful sleep..."
            
            scene black
            with Dissolve(3.5)

            jump cafe_day

        label cafe_day:
            scene bg bedroom:
                zoom 0.4
            with Dissolve(2) 
            
            "I groaned as the beeping of my alarm pulled me into consciousness. I blinked at the alarm blearily and was about to turn it off before I remembered my prior commitment to meet Mira."
            menu:
                "A few more minutes couldn't hurt...":
                    $ affection -= 10
                    $ slept_in = True
                    jump slept_in
                "I should get up, I don't want to keep Mira waiting.":
                    $ slept_in = False
                    $ affection += 10
                    "I ate a light breakfast, put on some clothing for the day and relaxed for a little while before it was time to go."
                    jump cafe

            label slept_in:
                "I turned off the alarm and went back to sleep."
                mc little sad "I'm sure Mira will be late anyway, what's the point in getting up now?"
                "I fell back asleep almost immediately."
                scene bg black
                with Dissolve(2)

                scene bg bedroom
                with Dissolve(2)

                "I awoke naturally some time later."
                mc smile "Ahh... I feel better rested."
                mc shocked "Wait, it's already 9:50? Oh geez, I need to go!"

                "I threw on clothes and raced out the door."
                jump cafe

            label cafe:
                play music "audio/music/cafe.mp3" fadeout 1 fadein 1
                scene bg cafe outside:
                    zoom 1.0
                    yalign 0.8
                with Dissolve(1)
                if slept_in:
                    "I arrived at the cafe almost 30 minutes late and, of course, this was the one time Mira was on time. She waved me down as I approached."

                    show mira shocked 
                    m "Is everything ok? You're running really late."

                    mc little sad "Yeah, I'm fine, I just slept in"

                    show mira sad
                    m "Well, I'm glad you're alright."

                    show mira smug
                    m "I guess I get a free drink today, huh?"

                    "Mira was playing it off, but I could tell she had been genuinely worried about me."

                else:
                    "I arrived at the cafe right on time, seeing Mira waiting outside."

                    show mira delighted
                    m "Hey [name], looks like I beat you today! Finally, free food for me!"

                    m "Now c'mon, the cats are getting cold!"

                    mc happy "I'm pretty sure that's not how that works."

                    "Mira tugged on my sleeve insistently, pulling me towards the cafe."
                    m "Sure it is! Now come oooonnn!"
                
                scene bg cafe inside
                with Dissolve(1)

                "We walked into the cat cafe, greeted by the tinkling of the door's bell and the low rumble of a purr."

                show grey cat flop:
                    yalign 0.8
                    xalign 0.3
                "A grey three-legged cat twined around Mira's legs as we walked up to the counter, then flopped on the floor when Mira reached down to pet him."

                show mira delighted at right behind grey
                "Awww, hi Yardstick! Happy to see me?"

                "Yardstick, aptly named for his three feet, was one of the owners cats so he was a permanent fixture. Mira had always been a favorite of his."

                show grey cat flop:
                    yalign 1.3
                    xalign 0.2
                show mira happy at left
                with move


                "Mira scratched behind his ears affectionately, then scooped him up and went to sit on a cozy sofa in the corner."

                m "Grab me whatever you think I would like!"

                hide mira
                hide grey cat
                with moveoutleft


                "I strolled up to the cafe's counter, pausing along the way to pet the inquisitive kitties that greeted me."
                "I contemplated what to get Mira."
                default snacks_opinion = 0

                menu:
                    "Which food do I pick for Mira?"
                    
                    "Some cream puffs":
                        $ affection += 0 
                        $ snacks_opinion +=0
                    "An orange scone":
                        $ affection -= 5
                        $ snacks_opinion -=1
                    "A chocolate eclair.":
                        $ affection += 5
                        $ snacks_opinion +=1
                    "A raspberry tart.":
                        $ affection +=5
                        $ snacks_opinion +=1
                    "A turkey and cheese sandwich.":
                        $ affection += 0
                        $ snacks_opinion +=0

                menu:
                    "Which drink do I order for Mira?"

                    "Steamed milk.":
                        $ affection += 0
                        $ snacks_opinion += 0
                    "A pumpkin-spice latte.":
                        $ affection += 5
                        $ snacks_opinion += 1
                    "A coffee, black.":
                        $ affection -= 5
                        $ snacks_opinion -=1
                    "Hot chocolate with whipped cream.":
                        $ affection += 5
                        $ snacks_opinion +=1
                    "Tea.":
                        $ affection += 0
                        $ snacks_opinion += 0
                
                show mira normal at center
                show grey cat sleep:
                    zoom 0.7
                    yalign 0.9
                    xalign 0.3

                show white cat curl:
                    zoom 0.8
                    yalign 0.8
                    xalign 0.7
                
                "Our order was ready soon enough and I brought it over to Mira."
                "Yardstick was flopped over in her lap, purring like a tiny motorboat. A white cat I hadn't seen before was curled up next to her, dozing contentedly."
                "I sat down next to Mira and handed her her food and drink."

                if snacks_opinion == 2:
                    show mira happy
                    m "Wow, you got exactly what I would have gotten! Thank you so much!"
                elif snacks_opinion == 1:
                    show mira happy
                    m "Not quite what I would have picked, but it's still pretty good!"
                elif snacks_opinion == 0:
                    show mira little sad
                    m "Well, uh, I guess this is ok."
                elif snacks_opinion == -1:
                    show mira sad
                    m "Oh, uh, I don't really like these."
                else:
                    show mira annoyed
                    m "Uh, did you deliberately pick things I hate for some reason?"
                
                show mira happy
                "Shortly after sitting down, the small white cat crawled over Mira's legs and sprawled over both of our laps. Mira giggled and stroked the cat's back."

                m "Her name is Mazipan, isn't she precious? You know, she's up for adoption..."

                mc annoyed "Mira, no, we've talked about this."

                m "But she's sooooo sweet and she really likes me!"

                mc "Mira. Your apartment doesn't allow pets."

                show mira sad
                m "I knoooow... I wish I could afford a pet-friendly place but so many of them around here have such high rent and then pet rent, and then the pet deposit..."

                show mira little sad
                "Mira rested her head on my shoulder with a sigh."
                m "Maybe some day."

                "Mira seemed really down, more so than usual. I knew she had cats as a kid and she hadn't been able to get one since moving out. Her apartment was small and largely undecorated and had always felt bit lonely to me."
                
                menu:
                    "\"Hey, why don't you tell me about that new show you've been watching?\"":
                        $ affection += 5
                        show mira happy
                        m "Oh yeah, the last episode was soooo good, oh my gosh! Princess Wonderbeam FINALLY told the Witch Crystal that she loves her! It was so dramatic! Ok, so, at the start of the episode..."
                        "Mira cheered up a bit as she told me about Princess Wonderbeam and the Pop Stars and Justice."
                        jump important_conversations

                    "\"It's ok that you're sad about it. I think you'll be able to get a cat someday, just not yet.\"":
                        $ affection += 10
                        show mira normal
                        m "Thanks, [name]. I think I really needed to hear that. It feels a little silly, but it's lonely in my apartment without anyone else there."
                        mc smile "It's not silly. My apartment feels lonely too sometimes."
                        show mira delighted
                        m " I guess we'll both have to come over more then, huh?"
                        mc happy "I guess so! Maybe we could decorate your place a little more too. What do you think you'd want to put in it?"

                        m "Oh! I had this great idea to wrap fairy lights around my bed posts and string them up the walls, and I thought that maybe I could..."
                        "Mira and I talked for a while about ways to make her apartment feel a little more like home."
                        jump important_conversations


                    "\"Is it really that big of a deal? You can just come to this cafe, right?\"":
                        $ affection -= 10
                        show mira sad
                        "Mira pulled back from my shoulder and wouldn't meet my eyes."
                        m "Well, I mean, I guess it's not that big of a deal. But it still doesn't feel great, I guess? I miss my parents cats and my apartment doesn't really feel like a home."
                        m "Maybe that's silly of me."

                        show mira normal
                        "Yardstick seemed to pick up on Mira's mood and butted his head against her hand, causing her to smile a little."
                        m "Thanks, buddy. You're such a sweet cat."
                        "She still wouldn't look at me and I got the sense that I had said something wrong."

                        "Mira pet Yardstick until he was content that she was doing better, then curled back up and went to sleep."
                        jump important_conversations


            label important_conversations:
                scene bg black with Dissolve(0.5)

                scene bg cafe inside
                show mira normal
                with Dissolve(0.5)

                "After finishing our food and spending a long time cuddling the cats in the cafe, I realized that I wanted to talk to Mira."
                "Not just chat like we normally did; rather, there was something important I wanted to tell her."

                mc little sad "Hey, Mira?"

                m "Hmm? What is it, [name]?"
                mc little sad "I just wanted to tell you..."

                default ending = "good"

                if not date:
                    mc smile "You're my best friend and I love you so much. I'm so lucky to know you and I just wanted to tell you how much I appreciate you."
                    if affection >= 80:
                        show mira happy
                        m "Awww, [name], that's so sweet! Thank you! I love you too."
                        "Mira hugged me tightly."

                    elif affection <= 25:
                        show mira little sad
                        m "Oh, uh, that's nice of you!"
                        "Mira pointedly didn't say how she felt about me. An uncomfortable silence fell."
                        $ ending = "bad"

                    else:
                        show mira normal
                        m "Oh, thank you! You're pretty cool too!"
                        $ ending = "normal"

                elif date:
                    mc happy "I really like you as more than a friend and I wanted to know if you maybe wanted to try dating?"
                    if affection >= 80:
                        show mira happy
                        m "Aww, [name]! Yes, I've been trying to find the courage to ask! I would love to start dating and see where it goes."
                        "Mira hugged me tightly."
                        $ ending = "good"

                    elif affection <= 25:
                        show mira little sad
                        m "Oh, uh, ok. That's, uh, wow."
                        m "I, I don't really feel the same. Sorry."
                        mc little sad "Oh, ok. Got it."
                        "An uncomfortable silence fell."
                        $ ending = "bad"

                    else:
                        show mira normal
                        m "Oh, that's really flattering! We could give it a try."
                        $ ending = "normal"
                
                "Mira and I said our goodbyes and left the cafe."
                
            label ending:
                scene black with Dissolve(1)
                if ending == "bad":
                    "Mira and I grew apart as time went on. We just didn't connect like we used to."
                    "After a moth we stopped meeting regularly. After a few more months, we only saw each other briefly every few weeks. Conversations were strained and I could tell neither of us were comfortable."
                    "Finally, we fell out of contact entirely. I don't know where she is or what she's doing now. All I really know is that I don't have a place in her life anymore."
                elif ending == "normal":
                    if date:
                        "Mira and I tried dating for a while, but it didn't really work out between us. We both agreed that we were better friends than partners."
                        "However, Mira and I stayed friends after the break up and we still met up sometimes to catch up."
                        "Our lives may have shifted and dating may not have worked out, but I'm glad we're still friends."
                    else:
                        "Mira and I stayed friends. We weren't the best of friends, but we still met up to catch up and talk about our lives."
                        "Even though we're not as close as we used to be, I'm still glad Mira's a part of my life."
                else:
                    if date:
                        "Mira and went on our first date shortly after that. We took it slow at the start, doing what we normally did but wth a new label."
                        "It was clear to both of us that there was a strong connection. There always had been - the nature of it had just shifted."
                        "After a year, we decided to move in together. We were able to cover the cost of a pet-friendly apartment together and Mira was able to get cats like she had always wanted."
                        "Now, years later, I'm so glad that she's such a big part of my life. Our bond is stronger then ever and I can't see anything ever breaking it."
                    else:
                        "After telling Mira how much she meant to me, we decided together that we wanted to meet up more regularly. We enjoyed spending time together so much, it only made sense."
                        "After a year, we decided to move in together. We were able to cover the cost of a pet-friendly apartment together and Mira was able to get cats like she had always wanted."
                        "Now, years later, I'm so glad that she's such a big part of my life. Our bond is stronger then ever and I can't see anything ever breaking it."
                "The End."
                "Thanks for playing!"


                        
                

    # This ends the game.

    return
