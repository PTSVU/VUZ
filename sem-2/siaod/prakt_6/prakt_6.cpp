#include <iostream>
#include <string>
using namespace std;

long long step_counter_cf = 0, step_counter_mf = 0;
double time_spent;

void KnutSearch(string text, string search_word)
{
	bool suc = false;
	clock_t begin = clock();

    int m = text.length();
    int n = search_word.length();

    cout << endl << endl << m << endl << endl;

    if (m < n)
    {
        cout << "Pattern not found";
        return;
    }

    int *next = new int[n + 1];

    for (int i = 0; i < n + 1; i++) {
        next[i] = 0;
        step_counter_mf++;
    }

    for (int i = 1; i < n; i++)
    {
        int j = next[i + 1];
        while (j > 0 && search_word[j] != search_word[i]) {
            j = next[j];
        }

        if (j > 0 || search_word[j] == search_word[i]) {
            next[i + 1] = j + 1;
        }
        step_counter_mf++;
    }
    for (int i = 0, j = 0; i < m; i++)
    {
        if (text[i] == search_word[j])
        {
            step_counter_cf++;
            if (++j == n) {
                cout << "\n\tIndex word= " << i - j + 1 << endl;
                cout << "\n\tCF+MF= " << step_counter_cf + step_counter_mf << "\n\n";
            }
        }
        else if (j > 0)
        {
            step_counter_cf++;
            j = next[j];
            i--;
        }
    }

	clock_t end = clock();
	time_spent += (double)(end - begin) / CLOCKS_PER_SEC;
	cout << "\n\tTime= " << time_spent << "\n\n";
}

int main()
{
	string search_word, text;
    //243
    text = "The waves crashed against the shore, sending up a spray of salty water that glistened in the moonlight. The sound was soothing, and for a moment, I forgot about all of my troubles and just let myself be carried away by the rhythm of the ocean.";
    search_word = "sound";
    KnutSearch(text, search_word);
    //252
    text = "The wind howled through the deserted streets, whipping up dust and debris in its wake. A lone figure huddled against the wall, clutching a tattered coat around his body. He shivered as the cold seeped into his bones, wondering how he had ended up here.";
    search_word = "howled";
    KnutSearch(text, search_word);
    //328
    text = "He thought about the nature of love, and how it could be both the greatest joy and the deepest sorrow. He thought about the beauty of nature, and how it had sustained him through some of the darkest times in his life. And he thought about the power of hope, and how it had carried him through some of the most difficult moments.";
    search_word = "life";
    KnutSearch(text, search_word);
    //362
    text = "Help me, I'm being forced to write this awful text for some practical work before I have a gun to my temple, I want to write this text if anyone is reading this... HELP ME I'M LOCKED UP THIS MANIAC HAS ME ON..... This is all a joke, no one is forcibly holding me anywhere, I am writing this text completely in my right mind, I was just bored, so I amused myself.";
    search_word = "gun";
    KnutSearch(text, search_word);
    //1750
    text = "The sky was a deep shade of blue, the color of forget-me-nots and summer afternoons. The sun was high in the sky, casting a warm glow over everything below. The fields stretched out before me, a patchwork of greens and golds that swayed in the gentle breeze. In the distance, I could see the mountains, their peaks still snow-capped even in the heat of summer. I walked through the fields, the grass brushing against my bare legs.I felt free, alive, like anything was possible.I had nowhere to be, nothing to do but enjoy the beauty of the world around me.The wind blew through my hair, carrying with it the scent of wildflowers and earth. I lay down in the grass, feeling its softness against my skin.I closed my eyes and listened to the sounds of the world around me.The chirping of crickets, the rustling of leaves, the distant call of a bird.It was a symphony of life, a reminder that I was just one small part of something much bigger than myself. As I lay there, I thought about all of the things I wanted to do with my life.I wanted to see the world, to experience new cultures and ways of life.I wanted to create, to write stories that would inspire others, to make something beautiful out of the chaos of the world. But most of all, I wanted to love.I wanted to find someone who would understand me, who would accept me for who I was, flaws and all.I wanted to build a life with that person, to share all of the joys and sorrows that life had to offer. As the sun began to set, I knew that it was time to go home.But as I walked back through the fields, I felt a sense of peace in my heart.The world was a beautiful place, full of wonders and mysteries.And I knew that as long as I kept walking, kept exploring, kept loving, I would be okay.";
    search_word = "wind";
    KnutSearch(text, search_word);
}