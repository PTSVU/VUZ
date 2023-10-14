#include "cl_application.h"

void setConnections();

cl_application::cl_application(cl_base* p_head_object) : cl_base(p_head_object) {}

void cl_application::build_tree_objects()
{
	string s_head, s_sub;
	int s_num_obj;
	cl_base* p_head = this, * p_sub = nullptr;
	cin >> s_head;
	set_name(s_head);
	while (true)
	{
		cin >> s_head;
		if (s_head == "endtree")
		{
			break;
		}
		cin >> s_sub >> s_num_obj;
		if (p_head != nullptr)
		{
			p_head = find_obj_by_coord(s_head);
			switch (s_num_obj)
			{
			case 1:
				p_sub = new cl_1(p_head, s_sub);
				break;
			case 2:
				p_sub = new cl_2(p_head, s_sub);
				break;
			case 3:
				p_sub = new cl_3(p_head, s_sub);
				break;
			case 4:
				p_sub = new cl_4(p_head, s_sub);
				break;
			case 5:
				p_sub = new cl_5(p_head, s_sub);
				break;
			case 6:
				p_sub = new cl_6(p_head, s_sub);
				break;
			}
		}
		else
		{
			cout << "Object tree";
			print_from_current();
			cout << endl << "The head object " << s_head << " is not found";
			exit(1);
		}
	}
}

void cl_application::build_commands()
{
	string line, command, coord, text;
	vector <TYPE_SIGNAL> SIGNALS_LIST =
	{
			SIGNAL_D(cl_1::signal_f),
			SIGNAL_D(cl_2::signal_f),
			SIGNAL_D(cl_3::signal_f),
			SIGNAL_D(cl_4::signal_f),
			SIGNAL_D(cl_5::signal_f),
			SIGNAL_D(cl_6::signal_f)
	};
	vector<TYPE_HANDLER> HANDLERS_LIST =
	{
			HANDLER_D(cl_1::handler_f),
			HANDLER_D(cl_2::handler_f),
			HANDLER_D(cl_3::handler_f),
			HANDLER_D(cl_4::handler_f),
			HANDLER_D(cl_5::handler_f),
			HANDLER_D(cl_6::handler_f)
	};
	while (true)
	{
		getline(cin, line);
		command = line.substr(0, line.find(' '));
		line = line.substr(line.find(' ') + 1, line.size() - 1);
		coord = line.substr(0, line.find(' '));
		text = line.substr(line.find(' ') + 1);
		if (command == "END")
		{
			break;
		}
		if (line == "")
		{
			continue;
		}
		cl_base* pSender = this->find_obj_by_coord(coord);
		if (pSender == nullptr)
		{
			cout << endl << "Object " << coord << " not found";
			continue;
		}
		if (command == "EMIT")
		{
			TYPE_SIGNAL signal = SIGNALS_LIST[pSender->number - 1];
			pSender->emit_signal(signal, text);
		}
		if (command == "SET_CONNECT")
		{
			cl_base* pReceiver = this->find_obj_by_coord(text);
			if (pReceiver == nullptr)
			{
				cout << endl << "Handler object " << text << " not found";
			}
			TYPE_SIGNAL signal = SIGNALS_LIST[pSender->number - 1];
			TYPE_HANDLER handler = HANDLERS_LIST[pReceiver->number - 1];
			pSender->set_connection(signal, pReceiver, handler);
		}
		if (command == "DELETE_CONNECT")
		{
			cl_base* pReceiver = this->find_obj_by_coord(text);
			if (pReceiver == nullptr)
			{
				cout << endl << "Handler object " << text << " not found";
			}
			else
			{
				TYPE_SIGNAL signal = SIGNALS_LIST[pSender->number - 1];
				TYPE_HANDLER handler = HANDLERS_LIST[pReceiver->number - 1];
				pSender->delete_connection(signal, pReceiver, handler);
			}
		}
		if (command == "SET_CONDITION") {
			int state = stoi(text);
			pSender->setState(state);
		}
	}
}

int cl_application::exec_app()
{
	cout << "Object tree";
	print_from_current();
	this->setConnections();
	build_commands();
	return 0;
}

void cl_application::setConnections()
{
	string senderCoord;
	string receiverCoord;
	cl_base* pSender;
	cl_base* pReceiver;
	vector<TYPE_SIGNAL> SIGNALS_LIST =
	{
			SIGNAL_D(cl_1::signal_f),
			SIGNAL_D(cl_2::signal_f),
			SIGNAL_D(cl_3::signal_f),
			SIGNAL_D(cl_4::signal_f),
			SIGNAL_D(cl_5::signal_f),
			SIGNAL_D(cl_6::signal_f)
	};
	vector<TYPE_HANDLER> HANDLERS_LIST =
	{
			HANDLER_D(cl_1::handler_f),
			HANDLER_D(cl_2::handler_f),
			HANDLER_D(cl_3::handler_f),
			HANDLER_D(cl_4::handler_f),
			HANDLER_D(cl_5::handler_f),
			HANDLER_D(cl_6::handler_f)
	};
	while (true)
	{
		cin >> senderCoord;
		if (senderCoord == "end_of_connections") break;
		cin >> receiverCoord;
		pSender = this->find_obj_by_coord(senderCoord);
		pReceiver = this->find_obj_by_coord(receiverCoord);
		TYPE_SIGNAL signal = SIGNALS_LIST[pSender->number - 1];
		TYPE_HANDLER handler = HANDLERS_LIST[pReceiver->number - 1];
		pSender->set_connection(signal, pReceiver, handler);
	}
}