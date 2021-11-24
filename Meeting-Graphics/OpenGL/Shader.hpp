#ifndef SHADER_HPP
#define SHADER_HPP

#include <GL/eglew.h>
#include <string>

class Shader
{
    public:
        GLuint id;

        Shader(const char * vertex_file, const char * fragment_file);

        void Activate();
        void Delete();

    private:

        std::string getFileContent(const char * filename);
};

#endif
