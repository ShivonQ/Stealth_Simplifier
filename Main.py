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

    outermost_loop_variable = True
    setup_menu_loop = True
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

    # add pcs to pool

    def add_NPC_to_pool():
        stats_list = []
        name = input('What is the Character\'s name?')
        stats_list.append(name)
        # TODO: Switch it so instead of "Character's" it actually says the name.
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
        return stats_list


    def add_PC_to_pool():
        # Add a detector for whatever symbol you keep the items in the file seperated by
        # Perhaps make this method return a list of values.  That way I can have PC just fill in the last 3 elements of NPC.  ERGO More succinct.

        pc_data_set = add_NPC_to_pool()

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
            while True:
                speed = int(input('What is the PC\'s speed in 5 foot intervals(5 or 10 or 15, etc...)?'))

                if (speed % 5) != 0:

                    print('That was not a valid speed, try again.)')
                elif (speed % 5) == 0:
                    pc_data_set.append(speed)
                    break
        except ValueError:
            print('That was not a valid number please enter an integer.')

        #         MAKE THE PC IS EVERYTHING WENT FINE
        new_pc = PC.PC(pc_data_set[0], pc_data_set[1], pc_data_set[2], pc_data_set[3], pc_data_set[4], pc_data_set[5])
        current_PC_pool.append(new_pc)

    def selections_display():
        print(tabulate(selected_PCs, headers=["Selected PC's"], tablefmt="pipe"))
        print(tabulate(selected_NPCs, headers=["Selected NPC's"], tablefmt="pipe"))

    def display_pc_pool():
        menu_counter = 0
        print('Currently created PC\'s\n--------------------------')
        for pc in current_PC_pool:
            menu_counter = menu_counter + 1
            print('{}) {}'.format(menu_counter, pc.name))

    def display_terrain_mods():
        print('---Terrain Modifiers---')
        print('1) No terrain modifier\n'
              '2) Noisy (scree, shallow or deep bog, undergrowth, dense rubble)\n'
              '3) Very noisy (dense undergrowth, deep snow)')

    def create_check_parameters():

        del check_parameters[:]
        while True:
            try:
                distance = int(input('How far are the PC\'s attempting to stealth, in feet?'))
                check_parameters.append(distance)
                break

            except ValueError:
                'That was not a Integer, please try again.'

            while True:
                display_speed_mod_options()
                speed_mod_choice = input('What is the Speed Modifier Option?')

                if speed_mod_choice in '123':
                    check_parameters.append(speed_mod_choice)
                    break

                else:
                    print('Please Choose An Option From the Menu')

            while True:
                display_terrain_mods()
                terrain_mod_choice = input('What type of terrain?')
                if terrain_mod_choice in '123':
                    check_parameters.append(terrain_mod_choice)
                    break
                else:
                    print('Please select an option from above.')
    def run_checks():
        list_of_rows=[]
        create_check_parameters()
        pcs_vs_npcs_checks()

    def display_speed_mod_options():
        print('---Speed Modifiers---')
        print('1) Moving Up To Half Speed (No Modifier)\n'
              '2) Moving Up To Full Speed (-5)\n'
              '3) Moving Full Speed or Faster (-20)\n')

    def pcs_vs_npcs_checks():
        terrain_modifier = 0
        speed_modifier = 0
        total_env_mods = 0
        row_result = []
        final_results = []
        distance = int(check_parameters[0])
        fastest_pc_speed = 0

        for pc in selected_PCs:
            if pc.speed > 0:
                fastest_pc_speed = pc.speed
                if check_parameters[1] == '1':
                    fastest_pc_speed%2

        if check_parameters[1] == '2':
            speed_modifier - 5
        elif check_parameters[1] == '3':
            speed_modifier - 20

        if check_parameters[2] == '2':
            terrain_modifier - 2
        elif check_parameters[2] == '3':
            terrain_modifier - 5
        total_env_mods-speed_modifier-terrain_modifier
        while distance >= 0:

            for pc in selected_PCs:
                del row_result[:]
                row_result.append(pc.name)

                for npc in selected_NPCs:

                    sneak_result = d20.d20.roll(d20, pc.sneak_mod-total_env_mods)
                    listen_result = d20.d20.roll(d20, npc.listen_mod)
                    hide_result = d20.d20.roll(d20, pc.hide_mod)
                    spot_result = d20.d20.roll(d20, npc.spot_mod)

                    if sneak_result > listen_result:
                        row_result.append('Sneak: Success')
                    else:
                        row_result.append('-----FAIL-----')

                    if hide_result > spot_result:
                        row_result.append('Hide:  Success')
                    else:
                        row_result.append('-----FAIL-----')
                final_results.append(row_result)
                distance-fastest_pc_speed

    def display_npc_pool():
        menu_counter = 0
        print('Currently created NPC\'s\n--------------------------')
        for npc in current_NPC_pool:
            menu_counter = menu_counter + 1
            print('{}) {}'.format(menu_counter, npc.name))

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
