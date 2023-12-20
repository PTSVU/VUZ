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
            << "||" << setw(4) << "Product name" << setw(4)
            << "||" << setw(4) << "Product code" << setw(4)
            << "||" << setw(4) << "Manufacturer name" << setw(4)
            << "||" << setw(4) << "Price" << setw(4)
            << "||" << setw(4) << "Country" << setw(4) << "||\n\n";
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
        << "||" << setw(4) << "Product name" << setw(4)
        << "||" << setw(4) << "Product code" << setw(4)
        << "||" << setw(4) << "Manufacturer name" << setw(4)
        << "||" << setw(4) << "Price" << setw(4)
        << "||" << setw(4) << "Country" << setw(4) << "||\n\n";
    for (int i = 1; i < id.size(); i++)
    {
        textFile << "||" << setw(4) << id[i] << setw(4)
            << "||" << setw(4) << name[i] << setw(4)
            << "||" << setw(4) << code[i] << setw(4)
            << "||" << setw(4) << manufacturer[i] << setw(4)
            << "||" << setw(4) << price[i] << setw(4)
            << "||" << setw(4) << country[i] << setw(4) << "||\n";
    }
    textFile.close();
    txt_to_bin();
}

void Product::ProductAdd()
{
    string temp;
    double d_temp;
    while (true)
    {
        int ID = id[id.size() - 1] + 1;
        id.push_back(ID);
        cout << "\nВведите название продукта: ";
        cin >> temp;
        name.push_back(temp);
        cout << "\nВведите код продукта(не более 6 цифр): ";
        cin >> temp;
        while (temp.size() < 6)
        {
            temp = "0" + temp;
        }
        code.push_back(temp);
        cout << "\nВведите название изготовителя: ";
        cin >> temp;
        manufacturer.push_back(temp);
        cout << "\nВведите цену: ";
        cin >> d_temp;
        price.push_back(d_temp);
        cout << "\nВведите страну: ";
        cin >> temp;
        country.push_back(temp);
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
        << "||" << setw(4) << name[num] << setw(4)
        << "||" << setw(4) << code[num] << setw(4)
        << "||" << setw(4) << manufacturer[num] << setw(4)
        << "||" << setw(4) << price[num] << setw(4)
        << "||" << setw(4) << country[num] << setw(4) << "||\n";
}

void Product::DelCh(int num)
{
    vector <int>::iterator itId = id.begin();
    vector <string>::iterator itName = name.begin();
    vector <string>::iterator itCode = code.begin();
    vector <string>::iterator itManufacturer = manufacturer.begin();
    vector <double>::iterator itPrice = price.begin();
    vector <string>::iterator itCountry = country.begin();

    while (itId != id.end() ) {
        if (*itId == num) {
            id.erase(itId);
            name.erase(itName);
            code.erase(itCode);
            manufacturer.erase(itManufacturer);
            price.erase(itPrice);
            country.erase(itCountry);
            break;
        }
        itId++;
        itName++;
        itCode++;
        itManufacturer++;
        itPrice++;
        itCountry++;
    }

    string textFileName = fileName + ".txt";
    ofstream textFile(textFileName);
    textFile << "||" << setw(4) << "ID" << setw(4)
        << "||" << setw(4) << "Product name" << setw(4)
        << "||" << setw(4) << "Product code" << setw(4)
        << "||" << setw(4) << "Manufacturer name" << setw(4)
        << "||" << setw(4) << "Price" << setw(4)
        << "||" << setw(4) << "Country" << setw(4) << "||\n\n";
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
    cout << "\nВыбирете страну:" 
        << "\n\tЦифра - страна";
    vector <string> temp = { "" };
    bool ch = false;
    string con;
    int var;
    for (int i = 1; i < country.size(); i++)
    {
        for (int j = 1; j < temp.size(); j++)
        {
            if (temp[j] == country[i])
            {
                ch = true;
                break;
            }
        }
        if (ch == false)
        {
            cout << "\n\t" << i << " - " << country[i];
            temp.push_back(country[i]);
        }
        ch = false;
    }
    cout << "\n";
    cin >> var;
    con = country[var];
    string textFileName = fileName + "_" + con + ".txt";
    ofstream textFile(textFileName);
    textFile << "||" << setw(4) << "ID" << setw(4)
        << "||" << setw(4) << "Product name" << setw(4)
        << "||" << setw(4) << "Product code" << setw(4)
        << "||" << setw(4) << "Manufacturer name" << setw(4)
        << "||" << setw(4) << "Price" << setw(4)
        << "||" << setw(4) << "Country" << setw(4) << "||\n\n";
    for (int i = 1; i < country.size(); i++)
    {
        if (country[i] == con)
        {
            textFile << "||" << setw(4) << id[i] << setw(4)
                << "||" << setw(4) << name[i] << setw(4)
                << "||" << setw(4) << code[i] << setw(4)
                << "||" << setw(4) << manufacturer[i] << setw(4)
                << "||" << setw(4) << price[i] << setw(4)
                << "||" << setw(4) << country[i] << setw(4) << "||\n";
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
            double priceNum = stod(elements[4]);
            string countryName = elements[5];

            id.push_back(ID);
            name.push_back(productName);
            code.push_back(productCode);
            manufacturer.push_back(manufacturerName);
            price.push_back(priceNum);
            country.push_back(countryName);
        }
        if (elements.size() == 7) {
            int ID = stoi(elements[1]);
            string productName = elements[2];
            string productCode = elements[3];
            string manufacturerName = elements[4];
            double priceNum = stod(elements[5]);
            string countryName = elements[6];

            id.push_back(ID);
            name.push_back(productName);
            code.push_back(productCode);
            manufacturer.push_back(manufacturerName);
            price.push_back(priceNum);
            country.push_back(countryName);
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
        cout << "\n||" << setw(4) << "ID" << setw(4)
            << "||" << setw(4) << "Product name" << setw(4)
            << "||" << setw(4) << "Product code" << setw(4)
            << "||" << setw(4) << "Manufacturer name" << setw(4)
            << "||" << setw(4) << "Price" << setw(4)
            << "||" << setw(4) << "Country" << setw(4) << "||\n";
        PrintCh(var);
        cout << "\nЧто тут требуется изменить:"
            << "\n\t0 - перестать менять"
            << "\n\t1 - Product name"
            << "\n\t2 - Product code"
            << "\n\t3 - Manufacturer name"
            << "\n\t4 - Price"
            << "\n\t5 - Country\n";
        cin >> varr;
        switch (varr)
        {
        case 0:
            wh = false;
            break;
        case 1:
            cout << "Введите новое Product name\n";
            cin >> name[var];
            break;
        case 2:
            cout << "Введите новое Product code\n";
            cin >> code[var];
            while (code[var].size() < 6)
            {
                code[var] = "0" + code[var];
            }
            break;
        case 3:
            cout << "Введите новое Manufacturer name\n";
            cin >> manufacturer[var];
            break;
        case 4:
            cout << "Введите новое Price\n";
            cin >> price[var];
            break;
        case 5:
            cout << "Введите новое Country\n";
            cin >> country[var];
            break;
        default:
            wh = false;
            break;
        }
        TxtSave(var);
    }
}