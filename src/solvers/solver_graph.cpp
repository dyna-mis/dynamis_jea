#include "solver_graph.h"

void solver_graph::set(const shared_ptr<Problem>& P) {
	solver_ors::set(P);
	conflict_graph.set(problem_ref->point_size());
	set_graph();

};
void solver_graph::set(const shared_ptr<rect_problem>& P) {
	solver_ors::set(P);
	conflict_graph.set(rect_problem_ref->point_size());
	set_graph_rect();

};

bool solver_graph::add_point(const Point_2& p) {
	solver_ors::add_point(p);
	int index = problem_ref->point_size() - 1;

	std::list<Vertex_handle> LV;
	std::list<Vertex_handle>::const_iterator itv;
	unsigned v_index;
	rangeSearch_neighbor(pSet, p, LV);
	vector<int> neighbors;
	neighbors.clear();
	for (itv = LV.begin(); itv != LV.end(); itv++) {
		v_index = problem_ref->look_up((*itv)->point());
		if (v_index == index) continue;
		neighbors.push_back(v_index);
	}
	conflict_graph.add_vertex(index, neighbors);
	return true;
};


bool solver_graph::add_point_rect(const label_point& p) {
	solver_ors::add_point_rect(p);
	int index = rect_problem_ref->point_size() - 1;

	std::list<Vertex_handle> LV;
	std::list<Vertex_handle>::const_iterator itv;
	unsigned v_index;
	rangeSearch_neighbor(pSet, p, LV);
	vector<int> neighbors;
	neighbors.clear();
	for (itv = LV.begin(); itv != LV.end(); itv++) {
		v_index = look_up((*itv)->point());
		if (v_index == index) continue;
		neighbors.push_back(v_index);
	}
	conflict_graph.add_vertex(index, neighbors);
	return true;
}

bool solver_graph::delete_point(size_t index) {
	solver_ors::delete_point(index);
	conflict_graph.delete_vertex(index, problem_ref->point_size());
	return true;
};



bool solver_graph::delete_point_rect(size_t index) {
	solver_ors::delete_point_rect(index);
	conflict_graph.delete_vertex(index, rect_problem_ref->point_size());
	return true;
};



void solver_graph::set_graph() {
	std::list<Vertex_handle> LV;
	std::list<Vertex_handle>::const_iterator itv;
	unsigned v_index;
	for (unsigned u_index = 0; u_index < problem_ref->pVector.size(); u_index++) {
		rangeSearch_neighbor(pSet, problem_ref->pVector[u_index], LV);
		for (itv = LV.begin(); itv != LV.end(); itv++) {
			v_index = problem_ref->look_up((*itv)->point());
			if (v_index <= u_index) continue;
			else {
				conflict_graph.add_edge(u_index, v_index);
			}
		}
		LV.clear();
	}
};


void solver_graph::set_graph_rect() {
	std::list<Vertex_handle> LV;
	std::list<Vertex_handle>::const_iterator itv;
	unsigned v_index;
	for (unsigned u_index = 0; u_index < rect_problem_ref->pVector.size(); u_index++) {
		rangeSearch_neighbor(pSet, rect_problem_ref->pVector[u_index], LV);
		for (itv = LV.begin(); itv != LV.end(); itv++) {
			v_index = look_up((*itv)->point());
			if (v_index <= u_index) continue;
			else {
				conflict_graph.add_edge(u_index, v_index);
			}
		}
		LV.clear();
	}
}


//xPRINT+++++++++++++++PRINT+++++++++++++++++++++++++
#ifdef DYNAMIS_PRINT

void solver_graph::print()
{
	solver_ors::print();
	std::cout << "the conflict graph: " << std::endl;
	conflict_graph.print();
}
void solver_graph::print_rect()
{
	solver_ors::print_rect();
	std::cout << "the conflict graph: " << std::endl;
	conflict_graph.print();
}

#endif
//xPRINT---------------PRINT-------------------------


//!DEBUG+++++++++++++++debug++++++++++++++++++++++++
#ifdef DYNAMIS_DEBUG
void solver_graph::debug() {
	solver_ors::debug();
	conflict_graph.debug();
	int inConflict = 0;
	for (unsigned int u_index = 0; u_index < problem_ref->pVector.size(); u_index++) {
		for (unsigned int v_index = 0; v_index < problem_ref->pVector.size(); v_index++) {
			if (u_index == v_index) {
				assert(!conflict_graph.containEdge(u_index, v_index)); 
				continue;
			}
			inConflict = isConflict_debug(problem_ref->pVector[u_index], problem_ref->pVector[v_index]);
			if (inConflict == 0) continue;
			if (inConflict == 1) assert(conflict_graph.containEdge(u_index, v_index));
			if (inConflict == -1) assert(!conflict_graph.containEdge(u_index, v_index));
		}
	}
};

void solver_graph::debug_rect() {
	solver_ors::debug_rect();
	conflict_graph.debug();
	int inConflict = 0;
	bool inConflict_flag = false;
	for (unsigned int u_index = 0; u_index < rect_problem_ref->pVector.size(); u_index++) {
		for (unsigned int v_index = 0; v_index < rect_problem_ref->pVector.size(); v_index++) {
			if (u_index == v_index) { 
				assert(!conflict_graph.containEdge(u_index, v_index));
				continue; }
			inConflict = isConflict_debug(rect_problem_ref->pVector[u_index], rect_problem_ref->pVector[v_index]);
			if (inConflict == 0) continue;
			else {
				if (inConflict == 1) inConflict_flag = true;
				else inConflict_flag = false;
			}
			if (inConflict_flag != conflict_graph.containEdge(u_index, v_index)) {
				std::cout << "u_index:" << u_index << std::endl;
				std::cout << "v_index:" << v_index << std::endl;
				std::cout << "inConflict_flag:" << inConflict_flag << std::endl;
				std::cout << "containEdge" << conflict_graph.containEdge(u_index, v_index) << std::endl;
				print_point(rect_problem_ref->pVector[u_index]);
				print_point(rect_problem_ref->pVector[v_index]);
			}
			assert(inConflict_flag == conflict_graph.containEdge(u_index, v_index));
		}
	}
};

#endif
//!DEBUG---------------debug------------------------

