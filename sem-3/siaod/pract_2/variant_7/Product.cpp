#include "Product.h"

Product::Product()
{
    cout << "Введите название файла: ";
    cin >> fileName;
    if (fileName.empty())
    {
        fileName == "baseName";
    }
    string textFileName = fileName + ".txt";
    int var;
    if (fileExists(textFileName))
    {
        cout << "\nПерезаписать файл?\n\t0 - нет\n\t1 - да\n";
        cin >> var;
        if (var == 0)
        {
            vector_reconstruction();
        }
    } 
    if (!fileExists(textFileName) || var == 1)
    {
        ofstream textFile(textFileName);
        textFile << "||" << setw(4) << "ID" << setw(4)
            << "||" << setw(4) << "Spec code" << setw(4)
            << "||" << setw(4) << "Vuz name" << setw(4)
            << "||" << setw(4) << "Spec name" << setw(4) << "||\n\n";
        textFile.close();
    }
}

bool Product::fileExists(const string& filename) {
    ifstream file(filename.c_str());
    return file.good();
}

void Product::TxtSave(int num)
{
    string textFileName = fileName + ".txt";
    ofstream textFile(textFileName);
    textFile << "||" << setw(4) << "ID" << setw(4)
        << "||" << setw(4) << "Spec code" << setw(4)
        << "||" << setw(4) << "Vuz name" << setw(4)
        << "||" << setw(4) << "Spec name" << setw(4) << "||\n\n";
    for (int i = 1; i < id.size(); i++)
    {
        textFile << "||" << setw(4) << id[i] << setw(4)
            << "||" << setw(4) << specCode[i] << setw(4)
            << "||" << setw(4) << vuzName[i] << setw(4)
            << "||" << setw(4) << specName[i] << setw(4) << "||\n";
    }
    textFile.close();
    txt_to_bin();
}

void Product::ProductAdd()
{
    string temp;
    while (true)
    {
        int ID = id[id.size() - 1] + 1;
        id.push_back(ID);
        cout << "\nКод специальности: ";
        cin >> temp;
        specCode.push_back(temp);
        cout << "\nНазвание вуза: ";
        cin >> temp;
        vuzName.push_back(temp);
        cout << "\nНазвание специальности: ";
        cin >> temp;
        specName.push_back(temp);
        TxtSave(ID);
        cout << "\nПродолжить? (0 - нет, 1 - да)\n";
        cin >> temp;
        if (temp == "0")
        {
            break;
        }
    }
    cout << "\nВвод остановлен\n";
}

void Product::print_bin() {
    string binaryFilename = fileName + ".bin";

    ifstream binaryFile(binaryFilename, ios::in | ios::binary);

    string line;
    while (getline(binaryFile, line)) {
    }
    binaryFile.close();
    cout << line;
}

void Product::print_txt() {
    string textFilename = fileName + ".txt";

    ifstream textFile(textFilename);

    string line;
    while (getline(textFile, line)) {
        cout << line + "\n";
        line = "";
    }
    textFile.close();
}

void Product::bin_to_txt(string saveName) {
    string textFilename = saveName + ".txt";
    string binaryFilename = fileName + ".bin";

    ifstream binaryFile(binaryFilename, ios::in | ios::binary);

    ofstream textFile(textFilename);

    string line;
    while (getline(binaryFile, line)) {
        textFile.write(line.c_str(), line.length());;
    }

    textFile.close();
    binaryFile.close();
}

void Product::txt_to_bin() {
    string textFilename = fileName + ".txt";
    string binaryFilename = fileName + ".bin";

    ifstream textFile(textFilename);

    ofstream binaryFile(binaryFilename, ios::out | ios::binary);

    string line;
    while (getline(textFile, line)) {
        binaryFile.write(line.c_str(), line.length());
    }

    textFile.close();
    binaryFile.close();
}

void Product::PrintCh(int num)
{
    cout << "||" << setw(4) << id[num] << setw(4)
        << "||" << setw(4) << specCode[num] << setw(4)
        << "||" << setw(4) << vuzName[num] << setw(4)
        << "||" << setw(4) << specName[num] << setw(4) << "||\n";
}

void Product::DelCh(int num)
{
    vector <int>::iterator itId = id.begin();
    vector <string>::iterator itName = specCode.begin();
    vector <string>::iterator itCode = vuzName.begin();
    vector <string>::iterator itManufacturer = specName.begin();

    while (itId != id.end() ) {
        if (*itId == num) {
            id.erase(itId);
            specCode.erase(itName);
            vuzName.erase(itCode);
            specName.erase(itManufacturer);
            break;
        }
        itId++;
        itName++;
        itCode++;
        itManufacturer++;
    }

    string textFileName = fileName + ".txt";
    ofstream textFile(textFileName);
    textFile << "||" << setw(4) << "ID" << setw(4)
        << "||" << setw(4) << "Spec code" << setw(4)
        << "||" << setw(4) << "Vuz name" << setw(4)
        << "||" << setw(4) << "Spec name" << setw(4) << "||\n\n";
    textFile.close();

    for (int i = 1; i < id.size(); i++)
    {
        if (id[i] > num)
        {
            id[i] = id[i] - 1;
        }
        TxtSave(i);
    }
}

void Product::country_to_txt()
{
    cout << "\nВыбирете спецальность:" 
        << "\n\tЦифра - код спецальности";
    vector <string> temp = { "" };
    bool ch = false;
    string con;
    int var;
    for (int i = 1; i < specCode.size(); i++)
    {
        for (int j = 1; j < temp.size(); j++)
        {
            if (temp[j] == specCode[i])
            {
                ch = true;
                break;
            }
        }
        if (ch == false)
        {
            cout << "\n\t" << i << " - " << specCode[i];
            temp.push_back(specCode[i]);
        }
        ch = false;
    }
    cout << "\n";
    cin >> var;
    con = specCode[var];
    string textFileName = fileName + "_" + con + ".txt";
    ofstream textFile(textFileName);
    textFile << "||" << setw(4) << "ID" << setw(4)
        << "||" << setw(4) << "Spec code" << setw(4)
        << "||" << setw(4) << "Vuz name" << setw(4)
        << "||" << setw(4) << "Spec name" << setw(4) << "||\n\n";
    for (int i = 1; i < specCode.size(); i++)
    {
        if (specCode[i] == con)
        {
            textFile << "||" << setw(4) << id[i] << setw(4)
                << "||" << setw(4) << specCode[i] << setw(4)
                << "||" << setw(4) << vuzName[i] << setw(4)
                << "||" << setw(4) << specName[i] << setw(4) << "||\n";
        }
    }
    textFile.close();
}

void Product::vector_reconstruction()
{
    string textFilename = fileName + ".txt";
    ifstream textFile(textFilename);

    string line;
    getline(textFile, line);

    while (getline(textFile, line)) {
        size_t pos = 0;
        vector<string> elements;
        while ((pos = line.find("||")) != string::npos) {
            elements.push_back(space_del(line.substr(0, pos)));
            line.erase(0, pos + 2);
        }

        if (elements.size() == 6) {
            int ID = stoi(elements[0]);
            string productName = elements[1];
            string productCode = elements[2];
            string manufacturerName = elements[3];

            id.push_back(ID);
            specCode.push_back(productName);
            vuzName.push_back(productCode);
            specName.push_back(manufacturerName);
        }
        if (elements.size() == 7) {
            int ID = stoi(elements[1]);
            string productName = elements[2];
            string productCode = elements[3];
            string manufacturerName = elements[4];
            double priceNum = stod(elements[5]);
            string countryName = elements[6];

            id.push_back(ID);
            specCode.push_back(productName);
            vuzName.push_back(productCode);
            specName.push_back(manufacturerName);
        }
    }
}

string Product::space_del(const string& str) {
    size_t first = str.find_first_not_of(' ');
    if (string::npos == first) {
        return str;
    }

    size_t last = str.find_last_not_of(' ');
    return str.substr(first, (last - first + 1));
}

void Product::change_inf(int var)
{
    int varr;
    bool wh = true;
    while (wh)
    {
        cout << "||" << setw(4) << "ID" << setw(4)
            << "||" << setw(4) << "Spec code" << setw(4)
            << "||" << setw(4) << "Vuz name" << setw(4)
            << "||" << setw(4) << "Spec name" << setw(4) << "||\n";
        PrintCh(var);
        cout << "\nЧто тут требуется изменить:"
            << "\n\t0 - перестать менять"
            << "\n\t1 - Spec code"
            << "\n\t2 - Vuz name"
            << "\n\t3 - Spec name\n";
        cin >> varr;
        switch (varr)
        {
        case 0:
            wh = false;
            break;
        case 1:
            cout << "Введите новое Spec code\n";
            cin >> specCode[var];
            break;
        case 2:
            cout << "Введите новое Vuz name\n";
            cin >> vuzName[var];
            break;
        case 3:
            cout << "Введите новое Spec name\n";
            cin >> specName[var];
            break;
        default:
            wh = false;
            break;
        }
        TxtSave(var);
    }
}