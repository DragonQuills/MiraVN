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

        play music "audio/peaceful.mp3" fadein 2

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

        mc smile "Sorry, Mira. What's in the bag?"

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

            jump leaving_park


        label more_pastries:
            m "I bought more of them!"

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

            "Unfortunately, Mira's apartment wasn't pet friendly, or she definitely would have adopted one. Although maybe that was a good thing - I had talked Mira out of getting a cat more times than I could count."

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

                jump go_home

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

            m "Remember, 10am sharp! If you're late you have to buy the drinks."

            mc smug "Yeah right, as if you're going to get there earlier than I am, Ms. Hour Late!"

            show mira annoyed
            "Mira stuck out her tongue at me and we both went our separate ways."
            hide mira
            with easeoutright

            scene bg park night
            with Dissolve(2)

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
                scene bg cafe outside:
                    zoom 0.9
                with Dissolve(1)
                if slept_in:
                    "I arrived at the cafe almost 30 minutes late and, of course, this was the one time Mira was on time. She waved me down as I approached."

                    show mira shocked 
                    m "Is everything ok? You're running really late."

                    mc little sad "Yeah, I'm fine, I just slept in"

                    show m sad
                    m "Well, I'm glad you're alright."

                    show mira smug
                    m "I guess I get a free drink today, huh?"

                else:
                    "I arrived at the cafe right on time, seeing Mira waiting outside."

                    mira delighted "Hey [name], looks like I beat you today! But I've only been here for a few minutes so I'll be generous and call it a tie."

            

                




    # This ends the game.

    return
