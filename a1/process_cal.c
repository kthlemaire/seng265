#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define MAX_LINE_LEN 200
#define MAX_EVENTS 1000

/*
    Stucture: event
    Stores: 
        description
        timezone
        lacation
        day
        month
        year
        day of the week
        start time 
        end_time
    of an event 
*/
struct Event
{
    char description[MAX_LINE_LEN];
    char timezone[MAX_LINE_LEN];
    char location[MAX_LINE_LEN];
    int day;
    int month;
    int year;
    char dweek[MAX_LINE_LEN];
    char start[MAX_LINE_LEN];
    char end[MAX_LINE_LEN];
};

void trim_word(char word[]);
int char_to_int(char word[]);
int read_file(char const *const file_name, struct Event events[]);
void get_dates(struct Event events[], char const *const start_date, char const *const end_date, int num_events);
void swap_events(struct Event events[], int i, int j);
void sort_events(struct Event events[], int events_counter);
void print_header(struct Event event, int events_last);
void print_events(struct Event events[], int events_counter);

/*
    Function: main
    Description: represents the entry point of the program.
    Inputs: 
        - argc: indicates the number of arguments to be passed to the program.
        - argv: an array of strings containing the arguments passed to the program.
    Output: an integer describing the result of the execution of the program:
        - 0: Successful execution.
        - 1: Erroneous execution.
*/
int main(int argc, char *argv[])
{

    /* Starting calling your own code from this point. */
    // Ideally, please try to decompose your solution into multiple functions that are called from a concise main() function.
    if (argc < 3)
    {
        exit(1);
    }
    char const *const start_date = argv[1];
    char const *const end_date = argv[2];
    char const *const file_name = argv[3];

    struct Event events[MAX_EVENTS];

    int num_events = read_file(file_name, events);
    if (num_events == 0)
    {
        exit(1);
    }
    get_dates(events, start_date, end_date, num_events);

    exit(0);
}

/* 
    Function: trim_word
    Description: Removes tags, in the form of <nameOfTag>, from a string. 
    Inputs: 
        - word: a string in the form of <nameOfTag>Element</nameOfTag>
    Outputs: 
        Void
*/
void trim_word(char word[])
{
    int before = 0;
    while (word[before] != '>')
    {
        before++;
    }

    for (int i = before + 1; i < strlen(word); i++)
    {
        word[i - before - 1] = word[i];
    }

    int j = 0;

    while (word[j] != '<')
    {
        j++;
    }
    word[j] = '\0';
}

/* 
    Function: char_to_int
    Description: Takes a string of numbers and returns the numbers as an integer
    Input: 
        - word: string of numbers
    Output: 
        - number in word as an integer
*/
int char_to_int(char word[])
{
    int x = atoi(word);
    return x;
}

/* 
    Function: read_file
    Description: Reads the events in a file and adds them to an array in the form of the events structure
    Input: 
        - file_name: A string in the form of "--file=file_name.xml"
        - events: an empty array of the event structure listed above
    Outputs: 
        - number of events read from the file
*/
int read_file(char const *const file_name, struct Event events[])
{
    char input[100];
    sscanf(file_name, "--file=%s", input);

    FILE *input_file = fopen(input, "r");
    if (input_file == NULL)
    {
        exit(1);
    }
    int num_events = 0;
    char holder[MAX_LINE_LEN];
    int temp = 0;
    int *pointTemp = &temp;
    fgets(holder, MAX_LINE_LEN, input_file);
    fgets(holder, MAX_LINE_LEN, input_file);

    while (fgets(holder, MAX_LINE_LEN, input_file) != NULL)
    {
        trim_word(holder);
        strcpy(events[num_events].description, holder);

        fgets(holder, MAX_LINE_LEN, input_file);
        trim_word(holder);
        strcpy(events[num_events].timezone, holder);

        fgets(holder, MAX_LINE_LEN, input_file);
        trim_word(holder);
        strcpy(events[num_events].location, holder);

        fgets(holder, MAX_LINE_LEN, input_file);
        trim_word(holder);
        temp = char_to_int(holder);
        events[num_events].day = temp;

        fgets(holder, MAX_LINE_LEN, input_file);
        trim_word(holder);
        temp = char_to_int(holder);
        events[num_events].month = temp;

        fgets(holder, MAX_LINE_LEN, input_file);
        trim_word(holder);
        temp = char_to_int(holder);
        events[num_events].year = temp;

        fgets(holder, MAX_LINE_LEN, input_file);
        trim_word(holder);
        strcpy(events[num_events].dweek, holder);

        fgets(holder, MAX_LINE_LEN, input_file);
        trim_word(holder);
        strcpy(events[num_events].start, holder);

        fgets(holder, MAX_LINE_LEN, input_file);
        trim_word(holder);
        strcpy(events[num_events].end, holder);

        fgets(holder, MAX_LINE_LEN, input_file);
        fgets(holder, MAX_LINE_LEN, input_file);

        num_events++;
    }

    fclose(input_file);

    return num_events;
}

/*
    Function: get_dates
    Description: For every day between the start_date and end_date, the function checks if there is an event
    on that day. The function adds the event to a new array of Events and passes that array to sort_events, 
    print_header and print_events to produce the correct output. 
    Input: 
        - events: an array of Events
        - start_date: a string in the form "--start=year/month/day"
        - end_date: a string in the form "--end=year/month/day"
        - num_events: the number of events in the array events
    Output: 
        void
*/
void get_dates(struct Event events[], char const *const start_date, char const *const end_date, int num_events)
{
    int start_day, start_month, start_year, end_day, end_month, end_year;
    sscanf(start_date, "--start=%4d/%2d/%2d", &start_year, &start_month, &start_day);
    sscanf(end_date, "--end=%4d/%2d/%2d", &end_year, &end_month, &end_day);

    int num_dates_last = 0;

    while ((end_year > start_year) || (end_year == start_year && end_month > start_month) || (end_year == start_year && end_month == start_month && end_day >= start_day))
    {
        char date[100];
        struct Event events_on_date[MAX_EVENTS];
        int events_on_date_counter = 0;

        for (int i = 0; i <= num_events; i++)
        {
            if (start_year == events[i].year && start_month == events[i].month && start_day == events[i].day)
            {
                events_on_date[events_on_date_counter] = events[i];
                events_on_date_counter++;
            }
        }

        if (events_on_date_counter != 0)
        {
            sort_events(events_on_date, events_on_date_counter);
            print_header(events_on_date[0], num_dates_last);
            print_events(events_on_date, events_on_date_counter);
            num_dates_last = events_on_date_counter;
        }

        if (start_day == 31 && start_month == 12)
        {
            start_day = 1;
            start_month = 1;
            start_year++;
        }
        else if (start_day == 31)
        {
            start_day = 1;
            start_month++;
        }
        else
        {
            start_day++;
        }
    }
}

/*
    Function: sort_events
    Description: Takes an array of Events that all occur on the same day and sorts them by the time they start. 
    Input: 
        - events: an array of Events that all occur on the same day
        - events_counter: the number of events in the array events
    Output: 
        void 
*/
void sort_events(struct Event events[], int events_counter)
{
    for (int i = 0; i < events_counter; i++)
    {
        int start_hour, start_minutes, compare_hour, compare_minutes;
        int holder = i;
        sscanf(events[i].start, "%02d:%02d", &start_hour, &start_minutes);

        for (int j = i; j < events_counter; j++)
        {
            sscanf(events[j].start, "%02d:%02d", &compare_hour, &compare_minutes);
            if (start_hour > compare_hour || (start_hour == compare_hour && start_minutes > compare_minutes))
            {
                start_hour = compare_hour;
                start_minutes = compare_minutes;
                holder = j;
            }
        }
        swap_events(events, i, holder);
    }
}

/*
    Function: swap_events
    Description: swaps two Events in an array of Events
    Input: 
        - events: array of Events
        - i: the index of the first event to be swapped
        - j: the index of the second event to be swapped
    Output: 
        void
*/
void swap_events(struct Event events[], int i, int j)
{
    struct Event temp = events[i];
    events[i] = events[j];
    events[j] = temp;
}

/* 
    Function: print_header
    Description: Takes an Event and prints a header in the form of: 
    <month> <day>, <year> (<day of the week>)
    -----------------------------------------
    Input: 
        - event: an Event
        - events_last: number of events that occured on a day before the given event
    Output: 
        void
*/
void print_header(struct Event event, int events_last)
{
    char months[12][10] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};
    char date[MAX_LINE_LEN];

    if (events_last != 0)
    {
        printf("\n\n");
        sprintf(date, "%s %d, %d (%s)", months[event.month - 1], event.day, event.year, event.dweek);
        printf("%s\n", date);
        for (int i = 0; i < strlen(date); i++)
        {
            printf("-");
        }
    }
    else
    {
        sprintf(date, "%s %d, %d (%s)", months[event.month - 1], event.day, event.year, event.dweek);
        printf("%s\n", date);
        for (int i = 0; i < strlen(date); i++)
        {
            printf("-");
        }
    }
}

/*
    Function: print_events
    Description: prints the events in an array of events in the form of: 
    <start time> to <end time>: <description> {{<location>}} | <timezone>
    Input: 
        - events: an array of Events
        - events_counter: the number of Events in events
    Output: 
        void
*/
void print_events(struct Event events[], int events_counter)
{
    for (int i = 0; i < events_counter; i++)
    {
        int start_hours, start_minutes, end_hours, end_minutes;
        sscanf(events[i].start, "%02d:%02d", &start_hours, &start_minutes);
        sscanf(events[i].end, "%02d:%02d", &end_hours, &end_minutes);
        char start_time[10];
        char end_time[10];
        if (start_hours > 12)
        {
            start_hours -= 12;
            sprintf(start_time, "%02d:%02d PM", start_hours, start_minutes);
        }
        else if (start_hours == 12)
        {
            sprintf(start_time, "%02d:%02d PM", start_hours, start_minutes);
        }
        else if (start_hours == 0)
        {
            start_hours = 12;
            sprintf(start_time, "%02d:%02d AM", start_hours, start_minutes);
        }
        else
        {
            sprintf(start_time, "%02d:%02d AM", start_hours, start_minutes);
        }
        if (end_hours > 12)
        {
            end_hours -= 12;
            sprintf(end_time, "%02d:%02d PM", end_hours, end_minutes);
        }
        else if (end_hours == 12)
        {
            sprintf(end_time, "%02d:%02d PM", end_hours, end_minutes);
        }
        else if (end_hours == 0)
        {
            end_hours = 12;
            sprintf(end_time, "%02d:%02d AM", end_hours, end_minutes);
        }
        else
        {
            sprintf(end_time, "%02d:%02d AM", end_hours, end_minutes);
        }

        printf("\n%s to %s: %s {{%s}} | %s", start_time, end_time, events[i].description, events[i].location, events[i].timezone);
    }
}