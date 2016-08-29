from tabulate import tabulate
import sys
import NPC
import PC
import d20


def main():
    print('Program is Running')
    current_PC_pool = []
    current_NPC_pool = []
    selected_PCs = []
    selected_NPCs = []
    check_parameters = []

    # TODO: Remove these 8 lines when working
    test_PC = PC.PC('Malcolm', 5, 5, 5, 5, 20)
    test_PC2 = PC.PC('Amy', 5, 5, 5, 5, 20)
    test_NPC = NPC.NPC('Guard1', 2, 2)
    test_NPC2 = NPC.NPC('Guard2', 2, 2)
    selected_PCs.append(test_PC)
    selected_PCs.append(test_PC2)
    selected_NPCs.append(test_NPC)
    selected_NPCs.append(test_NPC2)

    outermost_loop_variable = True
    # Follows are the various menus that the user will be navigating
    def display_main_menu():
        print('Welcome to the stealth simplifier app.'
                               '\nMore options to come in future editions.'
                               '\n----------'
                               '\n1)Setup and run stealth checks.'
                               '\n2)Exit program.')
    # One menu deep, this is where PCs and NPCs will be chosen and

    def display_setup_menu():
        print('----------'
              '\nSetup Menu'
              '\n----------'
              '\n1)Create PC\'s to add to the Current PC\'s Pool'
              '\n2)Create NPC\'s to add to the Current NPC\'s Pool')

        if current_PC_pool:
            print('3)Select PC from Current PC\'s Pool')

        if current_NPC_pool:
            print('4)Select NPC from Current NPC\'s Pool')

        if len(selected_NPCs) >= 1 and len(selected_PCs) >= 1:
            print('5)Run Stealth Checks with currently selected NPC\'s and PC\'s.')
            selections_display()
        print('X) Exit this menu to main menu.\n')

    def selections_display():
        print('---Selected PC\'s---')
        for pc in selected_PCs:
            print(pc.name)
        print('---Selected NPC\'s---')
        for npc in selected_NPCs:
            print(npc.name)

        # print(tabulate(selected_PCs, headers=["Selected PC's"], tablefmt="pipe"))
        # print(tabulate(selected_NPCs, headers=["Selected NPC's"], tablefmt="pipe"))


    def display_pc_pool():
        menu_counter = 0
        print('Currently created PC\'s\n--------------------------')
        for pc in current_PC_pool:
            menu_counter = menu_counter + 1
            print('{}) {}'.format(menu_counter, pc.name))

    def display_npc_pool():
        menu_counter = 0
        print('Currently created NPC\'s\n--------------------------')
        for npc in current_NPC_pool:
            menu_counter = menu_counter + 1
            print('{}) {}'.format(menu_counter, npc.name))


    def display_terrain_mods():
        print('---Terrain Modifiers---')
        print('1) No terrain modifier\n'
              '2) Noisy (scree, shallow or deep bog, undergrowth, dense rubble)\n'
              '3) Very noisy (dense undergrowth, deep snow)')

    def display_speed_mod_options():
        print('---Speed Modifiers---')
        print('1) Moving Up To Half Speed (No Modifier)\n'
              '2) Moving Up To Full Speed (-5)\n'
              '3) Moving Full Speed or Faster (-20)\n')


    # add pcs to pool

    def add_NPC_to_pool():
        stats_list = []
        name = input('What is the Character\'s name?')
        stats_list.append(name)
        # TODO: Switch it so instead of "Character's" it actually says the name.
        # I had to use seperate and repeating try/except/while loops to achieve the results I wanted.
        # I wanted the user to only have to input a single piece of information again should something be entered wrong.
        while True:
            try:
                spot_mod = int(input('What is the Character\'s Spot Modifier?'))
                stats_list.append(spot_mod)
                break
            except ValueError:
                print('That was not a valid number please enter an integer.')
        while True:
            try:
                listen_mod = int(input('What is the Character\'s Listen Modifier?'))
                stats_list.append(listen_mod)
                break
            except ValueError:
                print('That was not a valid number please enter an integer.')
        #         Pass these stats back out.  This is so that I could reuse this code for the PC createion as well.
        return stats_list


    def add_PC_to_pool():
        # TODO: Add a detector for whatever symbol you keep the items in the file seperated by once File Support is inlcuded

        # run the NPC creator, take the elements that it provides and then filll in the others.
        pc_data_set = add_NPC_to_pool()
        # while there is a ValueError exception, keep asking for data until they finally give you something correct.
        while True:
            # try:
            #     spot_mod = int(input('What is the PC\'s Spot Modifier?'))
            # except ValueError:
            #     print('That was not a valid number please enter an integer.')
            #
            # try:
            #     listen_mod = int(input('What is the PC\'s Listen Modifier?'))
            # except ValueError:
            #     print('That was not a valid number please enter an integer.')
            #
            try:
                sneak_mod = int(input('What is the PC\'s Move Silently Modifier?'))
                pc_data_set.append(sneak_mod)
                break
            except ValueError:
                print('That was not a valid number please enter an integer.')
        while True:
            try:
                hide_mod = int(input('What is the PC\'s Hide Modifier?'))
                pc_data_set.append(hide_mod)
                break
            except ValueError:
                print('That was not a valid number please enter an integer.')
        try:
            # Check for a value error, but more importantly...
            while True:
                speed = int(input('What is the PC\'s speed in 5 foot intervals(5 or 10 or 15, etc...)?'))
                # Check that the number they gave yyou is divisible by 5.  This is D&D Dammit not the real world.
                if (speed % 5) != 0:

                    print('That was not a valid speed, try again.)')
                elif (speed % 5) == 0:
                    pc_data_set.append(speed)
                    break
        except ValueError:
            print('That was not a valid number please enter an integer.')

        #         MAKE THE PC If EVERYTHING WENT FINE
        new_pc = PC.PC(pc_data_set[0], pc_data_set[1], pc_data_set[2], pc_data_set[3], pc_data_set[4], pc_data_set[5])
        # Add them to the pool of PCS
        current_PC_pool.append(new_pc)


    def create_check_parameters():
        # Empty the list of parameters so it is fresh.
        del check_parameters[:]
        while True:
            try:
                # Didtance?
                distance = int(input('How far are the PC\'s attempting to stealth, in feet?'))
                check_parameters.append(distance)
                break

            except ValueError:
                'That was not a Integer, please try again.'

        while True:
            # display options
            display_speed_mod_options()
            # speed modifiers for the roll
            speed_mod_choice = input('What is the Speed Modifier Option?')

            if speed_mod_choice in '123':
                check_parameters.append(speed_mod_choice)
                break

            else:
                print('Please Choose An Option From the Menu')

        while True:
            # Display Options
            display_terrain_mods()
            # terrain modifiers for the rolls?
            terrain_mod_choice = input('What type of terrain?')
            if terrain_mod_choice in '123':
                check_parameters.append(terrain_mod_choice)
                break
            else:
                print('Please select an option from above.')
        # return the parameters so that the next function can use them
        return check_parameters

    def run_checks():
        # Make the parameters
        check_params = create_check_parameters()
        # Pass them to the checks function (Which needs to be broken down further into even MORE discrete bits.)
        final_list = pcs_vs_npcs_checks(check_params)
        # Display the list or results using this nice and fancy tabulate module
        print(tabulate(final_list, headers=['PC', selected_NPCs[0].name, selected_NPCs[0].name, selected_NPCs[1].name, selected_NPCs[1].name],tablefmt="pipe", missingval='Null'))

    def pcs_vs_npcs_checks(check_parameters):
        # TODO: Make this smoother code in the future.
        terrain_modifier = 0
        speed_modifier = 0
        total_env_mods = 0
        row_result = []
        final_results = []
        distance = int(check_parameters[0])
        fastest_pc_speed = 0
        # For each character find out which is fastest, and use their speed for the checks since they will reach the destination first.
        # TODO: Put this in its own function (EASY)
        for pc in selected_PCs:
            if pc.speed > 0:
                fastest_pc_speed = pc.speed
                if check_parameters[1] == '1':
                    fastest_pc_speed = fastest_pc_speed / 2
                elif check_parameters[1] == '3':
                    fastest_pc_speed = fastest_pc_speed * 2
        # Figure out what those parameters that were passed to you even mean! These are for how fast they're moving
        if check_parameters[1] == '2':
            # Ah! theyre moving quickly, hard to be stealthy when quick! MINUS 5
            speed_modifier = speed_modifier - 5
        elif check_parameters[1] == '3':
            # Theyre literally running while trying to be stealthy.  nearly impossible. MINUS 20
            speed_modifier = speed_modifier - 20
        # These params are for the type of terrain theyre going over
        if check_parameters[2] == '2':
            # Sort of noisy terrain, MINUS 2
            terrain_modifier = terrain_modifier - 2
        elif check_parameters[2] == '3':
            # Fairly loud terrain, MINUS 5
            terrain_modifier = terrain_modifier - 5

        #     Add the modifiers together into a lump mod to be subtracted from the roll
        total_env_mods = total_env_mods - speed_modifier - terrain_modifier

        # This variable is improperly named, but wont be changed until v1.2
        # It was originally a checker for just 2 players stealthing, to see that the distance(or number of checks really)
        # Isnt changed until all the PC's have taken a check.  I realized later on that I could use the modulus of the length of the
        # selected_PCs list to more accurately track that, since I could have 5 players doing it, or just 1 even
        even_or_odd = 0
        # While the PCs are not at their end point
        while distance >= 0:
            # for each PC check their stealth and hides against
            for pc in selected_PCs:
                # This bit here is causing trouble, and I am getting repeat rows... not sure whats wrong with it...
                row_result = []
                # keep the tracker counting
                even_or_odd = even_or_odd + 1
                # Add the name to the results row
                row_result.append(pc.name)
                # Each of the NPC's looking and listening
                for npc in selected_NPCs:
                    # Make the PC's Checks
                    sneak_result = d20.d20.roll(d20, pc.sneak_mod-total_env_mods)
                    # and the NPCs checks
                    listen_result = d20.d20.roll(d20, npc.listen_mod)
                    # PC
                    hide_result = d20.d20.roll(d20, pc.hide_mod)
                    # NPC
                    spot_result = d20.d20.roll(d20, npc.spot_mod)
                    # COMPARE RESULTS TO SEE IF SPOTTED OR HEARD
                    if sneak_result > listen_result:
                        row_result.append('Sneak: Success')
                    else:
                        row_result.append('-----FAIL-----')

                    if hide_result > spot_result:
                        row_result.append('Hide:  Success')
                    else:
                        row_result.append('-----FAIL-----')
                #         Push the results out onto the display board
                final_results.append(row_result)
                # If each PC has gone, then subtract the speed they are going from distance remaining
                if even_or_odd % len(selected_PCs) == 0:
                    distance = distance-fastest_pc_speed
        #             return the final list to be tabulated
        return final_results

    #  This function allows a character to be selected, it has been generified to work on either the NPC list or the PC list
    def select_the_char(which_list):
        if which_list == 0:
            # This is going to take a NPC
            choice = int(input('Which Character to add to the selected list?'))
            npc = current_NPC_pool[choice-1]
            selected_NPCs.append(npc)
            del current_NPC_pool[choice-1]

        elif which_list == 1:
            # This will take a PC
            choice = int(input('Which PC to add to the selected list?'))
            pc = current_PC_pool[choice-1]
            selected_PCs.append(pc)
            del current_PC_pool[choice-1]

    #         removes all characters from the selected pool automatically
    def remove_all_chars_from_selected():
        counter = 0
        for pc in selected_PCs:
            current_PC_pool.append(pc)
            del current_PC_pool[counter]
            counter = counter + 1
        counter2 = 0
        for npc in selected_NPCs:
            current_NPC_pool.append(npc)
            del current_NPC_pool[counter2]
            counter2 = counter2 + 1

    # TODO: Put all of this below into a method as well. Maybe
    # Here begins the guts of the runtime components
    while outermost_loop_variable:
        display_main_menu()
        main_menu_choice = input('Please Choose An Option From Above.\n')

        if main_menu_choice == '1':
            setup_menu_loop = True
            print('ENTERING SETUP AND RUN')
            while setup_menu_loop:
                # Show the Setup Menu
                display_setup_menu()
                # User Selects and Option
                # TODO: Surely there is a better way to do menus.
                setup_menu_choice = input('Please Choose And Option From Above.\n')
                if setup_menu_choice == '1':
                    print('Running Add PC to Pool Method')
                    # Add a PC
                    add_PC_to_pool()
                elif setup_menu_choice == '2':
                    print('Running Add NPC to Pool Method')
                    # add an NPC
                    char_data_set = add_NPC_to_pool()
                    new_npc = NPC.NPC(char_data_set[0], char_data_set[1], char_data_set[2])
                    current_NPC_pool.append(new_npc)

                elif setup_menu_choice == '3' and len(current_PC_pool) >= 1:
                    print('Running Select a PC Method')
                    display_pc_pool()
                    select_the_char(1)

                elif setup_menu_choice == '4' and len(current_NPC_pool) >= 1:
                    print('Running Select a NPC Method')
                    display_npc_pool()
                    select_the_char(0)

                elif setup_menu_choice == '5' and len(selected_PCs) >= 1 and len(selected_NPCs) >= 1:
                    print('Running Checks with Tabulate OutPut')
                    run_checks()
                    remove_all_chars_from_selected()

                elif setup_menu_choice.lower() == 'x':
                    print('Exiting Setup Menu')
                    setup_menu_loop = False

        elif main_menu_choice == '2':
            # Version 2.0 will save some of these and allow editing of saved ones.
            print('EXITING PROGRAM\nFLUSHING ALL CURRENT PCS AND NPCS')
            sys.exit()
        else:
            print('Sorry, the option you selected either is not yet available or never will be.'
                  '\nPlease select a different option'
                  '\n')
main()
