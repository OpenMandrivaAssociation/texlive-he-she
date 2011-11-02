Name:		texlive-he-she
Version:	1.0
Release:	1
Summary:	Alternating pronouns to aid to gender-neutral writing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/he-she
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/he-she.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/he-she.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package implements a version of semi-automatic pronoun
switching for writing gender-neutral (and possibly annoying)
prose. It has upper- and lowercase versions of switching
pronouns for all case forms, plus anaphoric versions that
reflect the current gender choice.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/he-she/he-she.sty
%doc %{_texmfdistdir}/doc/latex/he-she/README
%doc %{_texmfdistdir}/doc/latex/he-she/he-she.pdf
%doc %{_texmfdistdir}/doc/latex/he-she/he-she.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
