#include "Shader.hpp"
#include <GLFW/glfw3.h>

#include <fstream>
#include <iostream>

std::string Shader::getFileContent(const char * filename)
{
    /*std::ifstream f(filename);
    std::string c;

    f.seekg(0, std::ios::end);
    c.reserve(f.tellg());
    f.seekg(0, std::ios::beg);

    c.assign((std::istreambuf_iterator<char>(f)),
            std::istreambuf_iterator<char>());

    f.close();

    return c;
    */
 
	std::ifstream in(filename, std::ios::binary);
	if (in.good())
	{
		std::string contents;
		in.seekg(0, std::ios::end);
		contents.resize(in.tellg());
		in.seekg(0, std::ios::beg);
		in.read(&contents[0], contents.size());
		in.close();
		return(contents);
	}

    return "";
}

Shader::Shader(const char * vertex_file, const char * fragment_file)
{
    std::string  vertex_source_str{getFileContent(vertex_file)};
    std::string  fragment_source_str{getFileContent(fragment_file)};

    auto vertex_source = vertex_source_str.c_str();
    auto fragment_source = fragment_source_str.c_str();

    // Vertex Shader
    GLuint vertexShader = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(vertexShader, 1, &vertex_source, NULL);
    glCompileShader(vertexShader);

    // Fragment Shader
    GLuint fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fragmentShader, 1, &fragment_source, NULL);
    glCompileShader(fragmentShader);

    id = glCreateProgram();

    glAttachShader(id, vertexShader);
    glAttachShader(id, fragmentShader);

    glLinkProgram(id);

    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);

}


void Shader::Activate()
{
    glUseProgram(id);
}

void Shader::Delete()
{
    glDeleteProgram(id);
}

