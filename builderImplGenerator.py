import spec

def upperCamel(s):
    return s[0].upper()+s[1:]

def generateStructH(st: spec.Struct):
    def genWith(param: spec.Param):
        return f'{st.name}Builder& With{upperCamel(param.name)}({param.tp} {param.name});'

    def genGet(param: spec.Param):
        return f'{param.tp} virtual Get{upperCamel(param.name)}() const;'
    return '\n'.join([
        f'class {st.name}Impl;',
        f'class {st.name} {{',
        f'public:',
    ] + [*map(lambda x: ' '*4+genGet(x), st.params)] + [
        f'    class {st.name}Builder {{',
        f'    public:',
        f'        {st.name}Builder();',
    ] + [*map(lambda x: ' '*8+genWith(x), st.params)] + [
        f'        std::shared_ptr<{st.name}> Build();',
        f'    private:',
        f'        std::shared_ptr<{st.name}Impl> m_prop;',
        f'    }};',
        f'}};',
        ''
    ])

def generateH(structs: 'list[spec.Struct]'):
    '''
        generate header file for structs using builder idiom
    '''
    return '\n'.join(map(generateStructH,structs))+'\n'

def generateStructHImpl(st):
    def genGet(param: spec.Param):
        return f'{param.tp} Get{upperCamel(param.name)}() const;'

    def genSet(param: spec.Param):
        return f'void Set{upperCamel(param.name)}({param.tp} {param.name});'
    def genMem(param: spec.Param):
        return f'{param.tp} {param.name};'

    return '\n'.join([
        f'class {st.name}Impl: public {st.name} {{',
        f'public:',
    ] + [*map(lambda x: ' '*4+genGet(x), st.params)] +
        [*map(lambda x: ' '*4+genSet(x), st.params)] + [
        f'private:',
    ] + [*map(lambda x: ' '*4+genMem(x), st.params)] + [
        f'}};',
        ''
    ])

def generateHImpl(structs):
    '''
        generate header file for impl
    '''
    return '\n'.join(map(generateStructHImpl,structs))+'\n'

def generateStructCpp(st):
    def genWith(param: spec.Param):
        return '\n'.join([
            f'{st.name}::{st.name}Builder& {st.name}::{st.name}Builder::With{upperCamel(param.name)}({param.tp} {param.name})',
            '{',
            f'    m_prop->Set{upperCamel(param.name)}({param.name});',
             '    return *this;',
            '}',
        ])
    return '\n'.join([
        f'{st.name}::{st.name}Builder::{st.name}Builder()',
         '{',
         '}',
    ] + [*map(genWith, st.params)] + [
        f'std::shared_ptr<{st.name}> {st.name}::{st.name}Builder::Build()',
         '{',
        f'    return m_prop;',
         '}',
    ])

def generateCpp(structs):
    '''
        generate cpp file for structs
    '''
    return '\n'.join(map(generateStructCpp,structs))+'\n'

def generateStructCppImpl(st):
    def genSet(param: spec.Param):
        return '\n'.join([
            f'void {st.name}Impl::Set{upperCamel(param.name)}({param.tp} {param.name})',
            '{',
            f'    this->{param.name} = {param.name};',
            '}',
        ])
    def genGet(param: spec.Param):
        return '\n'.join([
            f'{param.tp} {st.name}Impl::Get{upperCamel(param.name)}() const',
            '{',
            f'    return {param.name};',
            '}',
        ])
    return '\n'.join(
        [*map(genSet, st.params)] + [
    ] + [*map(genGet, st.params)] + [
    ])

def generateCppImpl(structs):
    '''
        generate cpp for impls
    '''
    return '\n'.join(map(generateStructCppImpl,structs))+'\n'

sts=[spec.Struct('A',[spec.Param('a','int',True,'description')])]

print('#include <memory>')
print(generateH(sts))
print(generateHImpl(sts))
print(generateCpp(sts))
print(generateCppImpl(sts))
