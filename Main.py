import tabulate
import sys
import NPC
import PC
import d20


def main():
    print('Program is Running')
    current_PC_pool = []
    current_NPC_pool = []
    selected_PCs=[]
    selected_NPCs=[]
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
        print('X) Exit this menu to main menu.\n')
    # add pcs to pool
    def add_NPC_to_pool():
        stats_list=[]
        name = input('What is the Character\'s name?')
        stats_list.append(name)
        while True:
            try:
                spot_mod = int(input('What is the Character\'s Spot Modifier?'))
                stats_list.append(spot_mod)
            except ValueError:
                print('That was not a valid number please enter an integer.')

            try:
                listen_mod = int(input('What is the Character\'s Listen Modifier?'))
                stats_list.append(listen_mod)
            except ValueError:
                print('That was not a valid number please enter an integer.')
            break
        return stats_list


    def add_PC_to_pool():
        # Add a detector for whatever symbol you keep the items in the file seperated by
        # Perhaps make this method return a list of values.  That way I can have PC just fill in the last 3 elements of NPC.  ERGO More succinct.

        char_data_set = add_NPC_to_pool()

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
                char_data_set.append(sneak_mod)
            except ValueError:
                print('That was not a valid number please enter an integer.')

            try:
                hide_mod = int(input('What is the PC\'s Hide Modifier?'))
                char_data_set.append(hide_mod)
            except ValueError:
                print('That was not a valid number please enter an integer.')

            try:
                while True:
                    speed = int(input('What is the PC\'s speed in 5 foot intervals(5 or 10 or 15, etc...)?'))

                    if (speed % 5) != 0:

                        print('Please enter a valid speed (in intervals of 5 feet 5,10,15, etc...)')
                    elif (speed % 5) == 0:
                        char_data_set.append(speed)
                        break
                break
            except ValueError:
                print('That was not a valid number please enter an integer.')
        #         MAKE THE PC IS EVERYTHING WENT FINE
        new_pc = PC.PC(char_data_set[0], char_data_set[1], char_data_set[2], char_data_set[3], char_data_set[4], char_data_set[5])
        current_PC_pool.append(new_pc)

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
                    NPC.NPC(char_data_set[0], char_data_set[1], char_data_set[2])
                elif setup_menu_choice == '3' and current_PC_pool == True:
                    print('Running Select a PC Method')

                elif setup_menu_choice == '4' and current_NPC_pool == True:
                    print('Running Select a NPC Method')

                elif setup_menu_choice == '5' and selected_PCs == True and selected_NPCs == True:
                    print('Running Checks with Tabulate OutPut')

                elif setup_menu_choice.lower() == 'x':
                    print('Exiting Setup Menu')
                    setup_menu_loop=False

        elif main_menu_choice == '2':
            # Version 2.0 will save some of these and allow editing of saved ones.
            print('EXITING PROGRAM\nFLUSHING ALL CURRENT PCS AND NPCS')
            sys.exit()
        else:
            print('Sorry, the option you selected either is not yet available or never will be.'
                  '\nPlease select a different option'
                  '\n')
main()
