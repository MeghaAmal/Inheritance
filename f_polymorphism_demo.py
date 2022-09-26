# This program demonstrates polymorphism.

import f_animals as animals

def main():
    # Create a Mammal object, a Dog object, and
    # a Cat object.
    mammal = animals.Mammal('regular animal')
    dog = animals.Dog()
    cat = animals.Cat()


    # Display information about each one.
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')
    # mammal.show_species()
    # mammal.make_sound()
    show_mammal_info(mammal)

    print()

    # dog.show_species()
    # dog.make_sound()
    show_mammal_info(dog)



    print()

    # cat.show_species()
    # cat.make_sound()
    show_mammal_info(cat)
    show_mammal_info('I am a string')


def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()

# Call the main function.
main()
